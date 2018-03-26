clear all;
close all;

% Initial number of random variables
n=10;
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
        deviation = arrayfun(@(x) (x-mu(i))^2, rv);
        std_dev(i) = sum(deviation)/(n*i-1);
        %Use of bootstrap to calculate the CI for the variance
        bootstrap = zeros(1,n*i);
        ci = zeros(1,R);
        for r = 1:R
            for j = 1:n*i
                pick = ceil(rand()*n*i);
                bootstrap(j) = rv(pick);
            end
            deviation = arrayfun(@(x) (x-mu(i))^2, bootstrap);
            ci(r) = sum(deviation)/(n*i-1);
        end
        ci = sort(ci);
        ci_low(i) = ci(r_0);
        ci_high(i) = ci(R+1-r_0);
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
plot(t,ci_high, '-.r');
grid on;
title('Confidence Intervals for the Variance using Uniform Distribution U(0,1)');
hold on;
plot(t,ci_low, '-.m');
xlabel('# of random variables');
ylabel('Confidence Intervals');
X = [t, fliplr(t)];
Y = [ci_high, fliplr(ci_low)];
fill(X, Y, 'y');
hold on;
plot(t,std_dev, '-b');
