clear all;
close all;

n=100;
num_exp = 100;

mu = zeros(1,num_exp);
ci_low = zeros(1,num_exp);
ci_high = zeros(1,num_exp);
count = 0;

for i=1:num_exp
    % Generate n=48 iid U(0,1) r.v.’s
    rv = rand(1,n);

    % Find sample mean, sample std dev and 95%-confidence interval for the mean
    mu(i) = mean(rv);

    % % Just to check, I calculated by-hand the sample mean, and it returns equal
    % sum_rv = sum(rv);
    % mu_sample = sum_rv/n;

    % sigma_sq = std(rv);

    % % Just to check, I calculated by-hand the sample standard deviation, and it returns equal
    % sum_dev = 0;
    % for i=1:n
    %     sum_dev = sum_dev + (rv(i) - mu)^2;
    % end
    % std_dev = sum_dev/n;
    deviation = arrayfun(@(x) (x-mu(i))^2, rv);
    std_dev = sum(deviation)/n;

    ci_low(i) = mu(i) - 1.96*sqrt(std_dev/n);
    ci_high(i) = mu(i) + 1.96*sqrt(std_dev/n);
    if(ci_low(i) > 0.5 || ci_high(i) < 0.5)
        count = count + 1;
    end
    n = n+100;
end

%Study the accuracy of the estimate with respect to the true value vs. n
err_from_true = abs(mu - 0.5);

%Plot the results
t = 100:100:100 + num_exp*99;
figure('Name', 'Experiment4');
plot(t,err_from_true, '-b');
xlabel('# of random variables');
ylabel('Squared error from the true value');
title('Accuracy of the mean of rvs')