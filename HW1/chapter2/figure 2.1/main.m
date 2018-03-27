close all;
clear all;

load('sgbdnew.dat');
load('sgbdold.dat');
sorted_old = sort(sgbdold);
sorted_new = sort(sgbdnew);

%Plot of Figure 2.1
t = 1:100;
figure('Name','Figure 2.1');
subplot(2,2,1);
plot(t,sgbdold,'+b');
ylim([0 200]);
yticks(linspace(0,200,5));
title('Old Values');

subplot(2,2,2);
plot(t,sgbdnew,'or');
ylim([0 200]);
yticks(linspace(0,200,5));
title('New Values');

subplot(2,2,3);
nbins = 10;
histogram(sgbdold,nbins);
xlim([0 200]);
xticks(linspace(0,200,5));
grid on;

subplot(2,2,4);
histogram(sgbdnew,nbins);
xlim([0 200]);
xticks(linspace(0,200,5));
grid on;

%Plot of Figure 2.2
t_2 = 1:200;
counter_old = zeros(1,200);
counter_new = zeros(1,200);
for i=1:200
	counter_old(i) = sum(sgbdold(:) <= i);
	counter_new(i) = sum(sgbdnew(:) <= i);
end

figure('Name','Figure 2.2');
plot(t_2,counter_old./length(sgbdold),'-b');
hold on;
plot(t_2,counter_new./length(sgbdnew),'-r');
xlim([0 200]);
ylim([0 1]);
legend('old', 'new');

%Plot of Figure 2.3
n=length(sgbdold);
%Old values
sample_median_old = (sorted_old(n/2) + sorted_old(n/2 + 1))/2;
% for the median p=0.5
p=0.5;
%I find the indexes of the CI for the median using a level of 95%
j = floor(n*p - 1.96*sqrt(n*p*(1-p)));
k = ceil(n*p + 1.96*sqrt(n*p*(1-p))) + 1;
ci_low_old = sorted_old(j);
ci_high_old = sorted_old(k);

%New Values
sample_median_new = (sorted_new(n/2) + sorted_new(n/2 + 1))/2;
% for the median p=0.5
p=0.5;
%I find the indexes of the CI for the median using a level of 95%
j = floor(n*p - 1.96*sqrt(n*p*(1-p)));
k = ceil(n*p + 1.96*sqrt(n*p*(1-p))) + 1;
ci_low_new = sorted_new(j);
ci_high_new = sorted_new(k);

%Plot for the median
x = [1 2];
y = [sample_median_old sample_median_new];
neg = y - [ci_low_old ci_low_new];
pos = [ci_high_old ci_high_new] - y;

figure('Name', 'Figure 2.3');
subplot(1,2,1);
errorbar(x, y, neg, pos, 'o');
title('Quantiles');
grid on;
ylim([0 200]);
yticks(linspace(0,200,5));
xlim([0 3]);
xticks([1 2]);
xticklabels({'Old', 'New'});

%CI for the mean
mu_old = mean(sgbdold);
mu_new = mean(sgbdnew);

var_old = sum((sgbdold-mu_old).^2)/n;
var_new = sum((sgbdnew-mu_new).^2)/n;
ci_high_old = mu_old + 1.96*sqrt(var_old/n);
ci_low_old = mu_old - 1.96*sqrt(var_old/n);
ci_high_new = mu_new + 1.96*sqrt(var_new/n);
ci_low_new = mu_new - 1.96*sqrt(var_new/n);

%Plot for the mean

y = [mu_old mu_new];
neg = y - [ci_low_old ci_low_new];
pos = [ci_high_old ci_high_new] - y;

subplot(1,2,2);
errorbar(x, y, neg, pos, 'o');
title('Mean and Standard Deviation');
grid on;
ylim([0 200]);
yticks(linspace(0,200,5));
xlim([0 3]);
xticks([1 2]);
xticklabels({'Old', 'New'});

%% Figure 2.8
var_old_unb = sum((sgbdold-mu_old).^2)/(n-1);
var_new_unb = sum((sgbdnew-mu_new).^2)/(n-1);
ci_high_old_unb = mu_old + 1.96*sqrt(var_old_unb/n);
ci_low_old_unb = mu_old - 1.96*sqrt(var_old_unb/n);
ci_high_new_unb = mu_new + 1.96*sqrt(var_new_unb/n);
ci_low_new_unb = mu_new - 1.96*sqrt(var_new_unb/n);


y = [mu_old mu_new];
neg = y - [ci_low_old ci_low_new];
pos = [ci_high_old ci_high_new] - y;
neg_unb = y - [ci_low_old_unb ci_low_new_unb];
pos_unb = [ci_high_old_unb ci_high_new_unb] - y;


gamma = 0.95;
r_0 = 25;
R = ceil(2*r_0/(1-gamma)) - 1;
bootstrap_old = zeros(1,length(sgbdold));
bootstrap_new = zeros(1,length(sgbdold));
mu_old_boot = zeros(1,R);
mu_new_boot = zeros(1,R);
for r = 1:R
    for j = 1:length(sgbdold)
        pick = ceil(rand()*length(sgbdold));
        bootstrap_old(j) = sgbdold(pick);
        bootstrap_new(j) = sgbdnew(pick);    
    end
    mu_old_boot(r) = mean(bootstrap_old);
    mu_new_boot(r) = mean(bootstrap_new);
end
mu_old_boot = sort(mu_old_boot);
mu_new_boot = sort(mu_new_boot);
ci_low_boot_old = mu_old_boot(r_0);
ci_high_boot_old = mu_old_boot(R+1-r_0);
ci_low_boot_new = mu_new_boot(r_0);
ci_high_boot_new = mu_new_boot(R+1-r_0);

neg_boot = y - [ci_low_boot_old ci_low_boot_new];
pos_boot = [ci_high_boot_old ci_high_boot_new] - y;

figure('Name', 'Figure 2.8');
errorbar([1 2], y, neg, pos, 'o');
hold on;
errorbar([1.2 2.2], y, neg_unb, pos_unb, 'o');
hold on;
errorbar([1.4 2.4], y, neg_boot, pos_boot, 'or');
title('Normal Asymptotic and Bootstrap Percentile Confidence Intervals');
ylim([0 70]);
xlim([0.9 2.5]);
xticks([1 2]);
legend('Normal', 'General', 'Bootstrap');