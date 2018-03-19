MATLAB is selecting SOFTWARE OPENGL rendering.

                            < M A T L A B (R) >
                  Copyright 1984-2017 The MathWorks, Inc.
                   R2017a (9.2.0.556344) 64-bit (glnxa64)
                               March 27, 2017

 
To get started, type one of these: helpwin, helpdesk, or demo.
For product information, visit www.mathworks.com.
 
>> addpath('/home/chewbecca/.emacs.d/elpa/matlab-mode-20180125.1010/toolbox','-begin'); rehash; emacsinit('emacsclient -n');
>> close all;
>> clear all;
>> load('sgbdnew.dat');
>> load('sgbdold.dat');
>> sorted_old = sort(sgbdold);
>> sorted_new = sort(sgbdnew);
>> t = 1:100;
>> figure('Name','Figure 2.1');
>> subplot(2,2,1);
Warning: MATLAB has disabled some advanced graphics rendering features by switching to software OpenGL. For more information, click <a
href="matlab:opengl('problems')">here</a>. 
>> plot(t,sgbdold,'+b');
>> ylim([0 200]);
>> yticks(linspace(0,200,5));
>> title('Old Values');
>> subplot(2,2,2);
>> plot(t,sgbdnew,'or');
>> ylim([0 200]);
>> yticks(linspace(0,200,5));
>> title('New Values');
>> subplot(2,2,3);
>> nbins = 10;
>> histogram(sgbdold,nbins);
>> xlim([0 200]);
>> xticks(linspace(0,200,5));
>> grid on;
>> close all;
>> clear all;
>> load('sgbdnew.dat');
>> load('sgbdold.dat');
>> sorted_old = sort(sgbdold);
>> sorted_new = sort(sgbdnew);
>> t = 1:100;
>> figure('Name','Figure 2.1');
>> subplot(2,2,1);
>> plot(t,sgbdold,'+b');
>> ylim([0 200]);
>> yticks(linspace(0,200,5));
>> title('Old Values');
>> subplot(2,2,2);
>> plot(t,sgbdnew,'or');
>> ylim([0 200]);
>> yticks(linspace(0,200,5));
>> title('New Values');
>> subplot(2,2,3);
>> nbins = 10;
>> histogram(sgbdold,nbins);
>> xlim([0 200]);
>> xticks(linspace(0,200,5));
>> grid on;
>> subplot(2,2,4);
>> histogram(sgbdnew,nbins);
>> xlim([0 200]);
>> xticks(linspace(0,200,5));
>> grid on;
>> t_2 = 1:200;
>> counter_old = zeros(1,200);
>> counter_new = zeros(1,200);
>> for i=1:200
counter_old(i) = sum(sgbdold(:) <= i);
counter_new(i) = sum(sgbdnew(:) <= i);
end
>> figure('Name','Figure 2.2');
>> plot(t_2,counter_old./length(sgbdold),'-b');
>> hold on;
>> plot(t_2,counter_new./length(sgbdnew),'-r');
>> xlim([0 200]);
>> ylim([0 1]);
>> legend('old', 'new');
>> n=length(sgbdold);
>> sample_median_old = (sorted_old(n/2) + sorted_old(n/2 + 1))/2;
>> p=0.5;
>> j = floor(n*p - 1.96*sqrt(n*p*(1-p)));
>> k = ceil(n*p + 1.96*sqrt(n*p*(1-p))) + 1;
>> ci_low_old = sorted_old(j);
>> ci_high_old = sorted_old(k);
>> sample_median_new = (sorted_new(n/2) + sorted_new(n/2 + 1))/2;
>> p=0.5;
>> ci_low_new = sorted_new(j);
>> ci_high_new = sorted_new(k);
>> x = [1 2];
>> y = [sample_median_old sample_median_new];
>> neg = y - [ci_low_old ci_low_new];
>> pos = [ci_high_old ci_high_new] - y;
>> figure('Name', 'Figure 2.3');
>> subplot(1,2,1);
>> errorbar(x, y, neg, pos, 'o');
>> title('Quantiles');
>> grid on;
>> ylim([0 200]);
>> yticks(linspace(0,200,5));
>> xlim([0 3]);
>> xticks([1 2]);
>> xticklabels({'Old', 'New'});
>> mu_old = mean(sgbdold);
>> mu_new = mean(sgbdnew);
>> deviation_old = arrayfun(@(x) (x-mu_old)^2, sgbdold);
>> var_old = sum(deviation_old)/n;
>> deviation_new = arrayfun(@(x) (x-mu_new)^2, sgbdnew);
>> var_new = sum(deviation_new)/n;
>> ci_high_old = mu_old + 1.96*sqrt(var_old/n);
>> ci_low_old = mu_old - 1.96*sqrt(var_old/n);
>> ci_high_new = mu_old + 1.96*sqrt(var_new/n);
>> ci_low_new = mu_old - 1.96*sqrt(var_new/n);
>> y = [mu_old mu_new];
>> neg = y - [ci_low_old ci_low_new];
>> pos = [ci_high_old ci_high_new] - y;
>> subplot(1,2,2);
>> errorbar(x, y, neg, pos, 'o');
>> title('Mean and Standard Deviation');
>> grid on;
>> ylim([0 200]);
>> yticks(linspace(0,200,5));
>> xlim([0 3]);
>> xticks([1 2]);
>> xticklabels({'Old', 'New'});
>> difference = sgbdold - sgbdnew;
>> figure('Name','Figure 2.7');
>> subplot(1,3,1);
>> plot(t,difference,'+k');
>> subplot(1,3,2);
>> histogram(difference,nbins);
>> sorted_diff = sort(difference);
>> sample_median_diff = (sorted_diff(n/2) + sorted_diff(n/2 + 1))/2;
>> ci_low_diff = sorted_diff(j);
>> ci_high_diff = sorted_diff(k);
>> neg = sample_median_diff - ci_low_diff;
>> pos = ci_high_diff - sample_median_diff;
>> subplot(1,3,3);
>> errorbar(1, sample_median_diff, neg, pos, 'o');
>> ylim([-100 200]);
>> hold on;
>> mu_diff = mean(difference);
>> deviation = arrayfun(@(x) (x-mu_diff)^2, difference);
>> var_diff = sum(deviation)/n;
>> ci_high_diff_mean = mu_diff + 1.96*sqrt(var_diff/n);
>> ci_low_diff_mean = mu_diff - 1.96*sqrt(var_diff/n);
>> plot([0 1 2], zeros(3,1)+mu_diff, '-b');
>> hold on;
>> plot([0 1 2], zeros(3,1)+ci_low_diff_mean, '-.b');
>> hold on;
>> plot([0 1 2], zeros(3,1)+ci_high_diff_mean, '-.b');
>> xlim([0 2]);
>> clear all;
>> close all;
>> n=48;
>> num_exp = 1000;
>> rv = zeros(num_exp,n);
>> mu = zeros(1,num_exp);
>> ci_low = zeros(1,num_exp);
>> ci_high = zeros(1,num_exp);
>> count = 0;
>> for i=1:num_exp
    rv(i,:) = rand(1,n);
    mu(i) = mean(rv(i,:));
    deviation = arrayfun(@(x) (x-mu(i))^2, rv(i,:));
    std_dev = sum(deviation)/n;
    ci_low(i) = mu(i) - 1.96*sqrt(std_dev/n);
    ci_high(i) = mu(i) + 1.96*sqrt(std_dev/n);
    if(ci_low(i) > 0.5 || ci_high(i) < 0.5)
        count = count + 1;
    end
end
>> sprintf('In %d experiments the confidence interval does not contains the true mean.', count)

ans =

    'In 43 experiments the confidence interval does not contains the true mean.'

>> [ci_low, sort_index] = sort(ci_low);
>> ci_high = ci_high(sort_index);
>> mu = mu(sort_index);
>> t = 1:1000;
>> figure('Name', 'Experiment2 Results');
>> plot(t,mu, '-b');
>> title('Confidence Intervals using Uniform Distribution U(0,1)');
>> hold on;
>> plot(t,ci_high, '-.r');
>> hold on;
>> plot(t,ci_low, '-.m');
>> legend('mean \mu','CI low', 'CI high')
>> grid on;
>> 