clear all;
close all;

n=1000;
num_exp = 1000;

rv = zeros(num_exp,n);
mu = zeros(1,num_exp);
ci_low = zeros(1,num_exp);
ci_high = zeros(1,num_exp);
count = 0;

for i=1:num_exp
    % Generate n=48 iid U(0,1) r.v.’s
    rv(i,:) = normrnd(0,1,[1 n]);

    % Find sample mean, sample std dev and 95%-confidence interval for the mean
    mu(i) = mean(rv(i,:));

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
    deviation = arrayfun(@(x) (x-mu(i))^2, rv(i,:));
    std_dev = sum(deviation)/(n-1);

    ci_low(i) = mu(i) - 1.96*sqrt(std_dev/n);
    ci_high(i) = mu(i) + 1.96*sqrt(std_dev/n);
    if(ci_low(i) > 0 || ci_high(i) < 0)
        count = count + 1;
    end
end

sprintf('In %d experiments the confidence interval does not contains the true mean.', count)
%Sort arrays based on ci_low
[ci_low, sort_index] = sort(ci_low);
ci_high = ci_high(sort_index);
mu = mu(sort_index);

%Plot the results
t = 1:1000;
figure('Name', 'Experiment2 Results');
plot(t,mu, '-b');
title('Confidence Intervals using Normal Distribution N(0,1)');
hold on;
plot(t,ci_high, '-.r');
hold on;
plot(t,ci_low, '-.m');
legend('mean \mu','CI low', 'CI high')
grid on;
