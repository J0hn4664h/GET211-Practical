voltage = 50;
resistance = [2 4 6 8 10 12];
power = [];

for rep = 1:length(resistance);
 power(rep) = (voltage^2)/resistance(rep);
end

plot(resistance, power);
ylabel("Power(W)");
xlabel("Resistance(Ω)");
title("Power variation with load");
