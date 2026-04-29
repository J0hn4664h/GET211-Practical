## Practical session 8

```m
voltage = 50;
resistance = [0 2 4 6 8 10];
power = [];

for rep = 1:length(resistance);
power(rep) = (voltage^2)/resistance(rep);
end

plot(resistance, power);
ylabel("Power(W)");
xlabel("Resistance(R)");
title("Power variation with load");
```
