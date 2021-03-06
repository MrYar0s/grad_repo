close all
clear variables
speedOfLight = 299792.458 %км/с
lambdaPr = 656.28 % нм

spectra = importdata('spectra.csv')
starNames = importdata('star_names.csv')
lambdaStart = importdata('lambda_start.csv')
lambdaDelta = importdata('lambda_delta.csv')

n_stars = size(starNames,1)

n_obs = size(spectra,1)
lambdaEnd = lambdaStart + (n_obs - 1)*lambdaDelta
lambda = (lambdaStart:lambdaDelta:lambdaEnd)'

i = 1;
speed = zeros(n_stars, 1);
while i <= n_stars
    s = spectra(:,i);
    [sHa, idx] = min(s);
    lambdaHa = lambda(idx);
    speed(i,1) = ((lambdaHa/lambdaPr) - 1) * speedOfLight;
    i = i + 1;
end
speed
movaway = starNames(speed>0)

fg = figure;
set(fg, 'Visible', 'on');
xlabel('Длина волны, нм');
ylabel(['Интенсивность, эрг/см^2/с/', char(197)])
title({'Спектры звёзд'})
grid on
hold on
for i = 1:1:n_stars
    s = spectra(:,i);
    if speed(i,1) < 0
       plot(lambda, s, "--", 'LineWidth', 1)
    end
    if speed(i,1) > 0
        plot(lambda, s, 'LineWidth', 3)
    end
end
legend(starNames, 'Location', 'northeast')
text(0.1, 0.9,'Ярослав Молоканов Б01-006','Units', 'normalized')
hold off
saveas(fg, 'spectra.png')