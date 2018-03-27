clear all;
close all;

% Initial number of random variables
n=100;
% Max number of rvs is n*num_samples
num_samples = 100;
% Confidence level
gamma = 0.95;
r_0 = 25;
R = ceil(2*r_0/(1-gamma)) - 1;

mu = zeros(1,num_samples);
std_dev = zeros(1,num_samples);
ci_low = zeros(1,num_samples);
ci_high = zeros(1,num_samples);
pi_low = zeros(1,num_samples);
pi_high = zeros(1,num_samples);
pi_low_boot = zeros(1,num_samples);
pi_high_boot = zeros(1,num_samples);
zeta = zeros(1,num_samples);
xi = zeros(1,num_samples);

for i=1:num_samples
	zeta(i) = chi2inv((1-gamma)/2,n*i-1);
	xi(i) = chi2inv((1+gamma)/2,n*i-1);
end

% disp(zeta);

for i=1:num_samples
		% Generate n=48 iid U(0,1) r.v.’s
		rv = normrnd(0,1,[1 n*i]);

		% Find sample mean, sample std dev and 95%-confidence interval for the variance
		mu(i) = mean(rv);
		std_dev(i) = sum((rv-mu(i)).^2)/(n*i-1);
		ci_low(i) = sqrt(std_dev(i)*zeta(i)/(n*i-1));
		ci_high(i) = sqrt(std_dev(i)*xi(i)/(n*i-1));
    pi_low(i) = mu(i) - 1.99*sqrt(std_dev(i));
    pi_high(i) = mu(i) + 1.99*sqrt(std_dev(i));
    
    bootstrap = zeros(R,n*i);
    for r = 1:R
        for j = 1:n*i
            pick = ceil(rand()*n*i);
            bootstrap(r,j) = rv(pick);
        end
    end
    bootstrap = sort(bootstrap, 2);
    mean_boot = mean(bootstrap, 1);
    pi_low_boot(i) = mean_boot(floor(n*i*(1-gamma)/2));
    pi_high_boot(i) = mean_boot(ceil(n*i*(1+gamma)/2));
end

%Study the accuracy of the estimate with respect to the true value vs. n
mean_err_from_true = abs(mu);
std_dev_err_from_true = abs(std_dev - 1);

%Plot the results
t = linspace(n, n*num_samples, num_samples);
figure('Name', 'Experiment4 - Accuracy');
subplot(1,2,1);
plot(t,mean_err_from_true, '-b');
grid on;
xlabel('# of random variables');
ylabel('Squared error from the true value');
title('Accuracy of the mean of rvs');
subplot(1,2,2);
plot(t,std_dev_err_from_true, '-b');
grid on;
xlabel('# of random variables');
ylabel('Squared error from the true value');
title('Accuracy of the variance of rvs');

figure('Name', 'Experiment4 - Confidence Intervals');
errorbar(t,std_dev, std_dev - ci_low, ci_high - std_dev, '-');
grid on;
title('Confidence Intervals for the Variance using Normal Distribution N(0,1)');
% $$$ hold on;
% $$$ plot(t,ci_low, '-.m');
xlabel('# of random variables');
ylabel('Confidence Intervals');
% $$$ X = [t, fliplr(t)];
% $$$ Y = [ci_high, fliplr(ci_low)];
% $$$ fill(X, Y, 'y');
% $$$ hold on;
% $$$ plot(t,std_dev, '-b');

figure('Name', 'Experiment4 - Prediction Intervals using theory');
errorbar(t, mu, mu - pi_low, pi_high - mu, '.');
grid on;
title('Prediction intervals at level 0.95 using theory with a N(0,1)');

figure('Name', 'Experiment4 - Prediction Interval using bootstrap');
errorbar(t, mu, mu - pi_low_boot, pi_high_boot - mu, '.');
grid on;
title('Prediction intervals at level 0.95 using bootstrap with a N(0,1)');