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
pi_low_th = zeros(1,num_samples);
pi_high_th = zeros(1,num_samples);
pi_low_boot = zeros(1,num_samples);
pi_high_boot = zeros(1,num_samples);
zeta = zeros(1,num_samples);
xi = zeros(1,num_samples);

for i=1:num_samples
    zeta(i) = chi2inv((1-gamma)/2,n*i-1);
    xi(i) = chi2inv((1+gamma)/2,n*i-1);
end

for i=1:num_samples
    % Generate n*i iid U(0,1) r.v.’s
    rv = rand(1,n*i);

    % Find sample mean, sample std dev and 95%-confidence interval for the variance
    mu(i) = mean(rv);
		std_dev(i) = sum((rv-mu(i)).^2)/(n*i-1);
    %Use of bootstrap to calculate the CI for the variance and PI
    bootstrap = zeros(1,n*i);
    ci = zeros(1,R);
    pi = zeros(1,R);
    for r = 1:R
        for j = 1:n*i
            pick = ceil(rand()*n*i);
            bootstrap(j) = rv(pick);
        end
        pi(r) = mean(bootstrap);
        ci(r) = sum((bootstrap-mu(i)).^2)/(n*i-1);
    end
    ci = sort(ci);
    ci_low(i) = ci(r_0);
    ci_high(i) = ci(R+1-r_0);
    pi = sort(pi);
    pi_low_boot(i) = pi(r_0);
    pi_high_boot(i) = pi(R+1-r_0);
    
    %Compute PI using theory (non normal distribution)
    rv_sorted = sort(rv);
    pi_low_th(i) = rv_sorted(floor(n*i*(1-gamma)/2)+1);
    pi_high_th(i) = rv_sorted(ceil(n*i*(1+gamma)/2)+1);
    
end

%Study the accuracy of the estimate with respect to the true value vs. n
err_from_true = abs(mu - 0.5);
std_dev_err_from_true = abs(std_dev - 1/12);

%Plot the results
t = linspace(n, n*num_samples, num_samples);
figure('Name', 'Experiment4 - Accuracy');
subplot(1,2,1);
plot(t,err_from_true, '-b');
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
errorbar(t, std_dev, std_dev-ci_low, ci_high-std_dev, '.');
grid on;
title('Confidence Intervals for the Variance using Uniform Distribution U(0,1)');
xlabel('# of random variables');
ylabel('Confidence Intervals');

figure('Name', 'Experiment4 - Prediction Intervals using theory');
errorbar(t, mu, mu - pi_low_th, pi_high_th - mu, '.');
grid on;
title('Prediction intervals at level 0.95 using theory');

figure('Name', 'Experiment4 - Prediction Interval using bootstrap');
errorbar(t, mu, mu - pi_low_boot, pi_high_boot - mu, '.');
grid on;
title('Prediction intervals at level 0.95 using bootstrap');