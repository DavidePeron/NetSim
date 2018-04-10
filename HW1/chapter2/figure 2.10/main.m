clear all;
close all;

load('joe.dat');

%Plot 10.a
figure(1);
plot(joe,'-k');
title('Data');
%Plot 10.c
% figure(2);
joe_inv = fliplr(joe);
joe_inv = conj(joe_inv);
acf = conv(joe, joe_inv)/(joe'*joe);
figure(2)
stem(acf, 'Marker', 'none');
title('Autocorrelation');
ylim([-0.6 1]);

%% Lag plots
figure(3);
for i=1:9
    subplot(3,3,i);
    joe_shifted = circshift(joe,i);
    plot(joe_shifted, joe, '.k');
    title(['h = ' num2str(i)]);
    xlim([-500 500]);
    ylim([-400 400]);
end
