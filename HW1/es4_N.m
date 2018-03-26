clear all;
close all;

% Initial number of random variables
n=10;
% Max number of rvs is n*num_samples
num_samples = 100;
% #experiments for each sample
num_exp = 100;
% Confidence level
gamma = 0.95;

mu = zeros(num_exp,num_samples);
std_dev = zeros(num_exp,num_samples);
ci_low = zeros(num_exp,num_samples);
ci_high = zeros(num_exp,num_samples);
pi_low = zeros(num_exp,num_samples);
pi_high = zeros(num_exp,num_samples);
zeta = zeros(1,num_samples);
xi = zeros(1,num_samples);

for i=1:num_samples
	zeta(i) = chi2inv((1-gamma)/2,n*i-1);
	xi(i) = chi2inv((1+gamma)/2,n*i-1);
end

% disp(zeta);

for i=1:num_samples
	for j= 1:num_exp
		% Generate n=48 iid U(0,1) r.v.’s
		rv = normrnd(0,1,[1 n*i]);

		% Find sample mean, sample std dev and 95%-confidence interval for the variance
		mu(j,i) = mean(rv);
		deviation = arrayfun(@(x) (x-mu(j,i))^2, rv);
		std_dev(j,i) = sum(deviation)/(n*i-1);
		ci_low(j,i) = sqrt(std_dev(j,i)*zeta(i)/(n*i-1));
		ci_high(j,i) = sqrt(std_dev(j,i)*xi(i)/(n*i-1));
    pi_low(j,i) = mu(j,i) - 1.99*sqrt(std_dev(j,i));
    pi_high(j,i) = mu(j,i) + 1.99*sqrt(std_dev(j,i));
	end
end

mean_mu = mean(mu,1);
mean_std_dev = mean(std_dev,1);
mean_ci_low = mean(ci_low,1);
mean_ci_high = mean(ci_high,1);
mean_pi_low = mean(pi_low,1);
mean_pi_high = mean(pi_high,1);

%Study the accuracy of the estimate with respect to the true value vs. n
mean_err_from_true = abs(mean_mu);
std_dev_err_from_true = abs(mean_std_dev - 1);

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
plot(t,mean_ci_high, '-.r');
grid on;
title('Confidence Intervals for the Variance using Normal Distribution N(0,1)');
hold on;
plot(t,mean_ci_low, '-.m');
xlabel('# of random variables');
ylabel('Confidence Intervals');
X = [t, fliplr(t)];
Y = [mean_ci_high, fliplr(mean_ci_low)];
fill(X, Y, 'y');
hold on;
plot(t,mean_std_dev, '-b');

figure('Name', 'Experiment4 - Prediction Intervals');
errorbar(t, mean_mu, mean_mu - mean_pi_low, mean_pi_high - mean_mu, '.');
grid on;
title('Prediction intervals at level 0.95 using theory');