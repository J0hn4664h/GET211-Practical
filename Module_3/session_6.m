for i = 1:5;
 disp(i);
end

j = 1
while j <= 5;
 disp(j);
 j = j + 1;
end0

readings = [10 20 30 40 50];
sum = 0;

for a = 1:length(readings);
 sum = sum + readings(a);
end

average = sum/length(readings);

disp(average);

k = 1;
total = 0;

while k <= length(readings);
 total = total + readings(k);
 k = k+1;
end

mean = total/length(readings); 

disp(mean);
