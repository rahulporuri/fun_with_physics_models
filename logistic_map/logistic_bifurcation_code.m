% Create file in which data will be stored.
fid = fopen('logistic_map_data.m', 'w');

% Print info on data to be stored:

% Calculate number of rows that will be stored in the file. This depends on the iterations of m and x. LOOK AT THE ITERATION BELOW, FOR A BETTER UNDERSTANDING!
m1 = 3;			% Initial m value.
m2 = 4;			% Fnitial m value.
dm = 0.001;		% Jump is m value in each iteration.

x1 = 0.1;		% Initial x value.
x2 = 0.9;		% Fnitial x value.
dx = 0.01;		% Jump is x value in each iteration.

R = ((m2 - m1 + dm)/dm) * ((x2 - x1 + dx)/dx);

fprintf(fid,'# name: C\n');				% Use this name to call data in this file.
fprintf(fid,'# type: matrix\n');	% Type of data.
fprintf(fid,'# rows: %d\n', R);				% Number of rows.
fprintf(fid,'# columns: 2\n');		% Number of columns.


for m=m1:dm:m2	% Iterate over values of logistic map parameter m.
    for x = x1:dx:x2	% Iterate over initial condition.
        for ii=1:500	% Iterate over time.
            x = m*x*(1-x);	% Logistic map equation.
        end
        % Print in file:
        fprintf(fid,'%f \t %f \n', m, x);
    end
end

fclose(fid);

% Load data generated earlier.
load logistic_map_data.m;

plot(C(:,1),C(:,2),'.', 'MarkerSize', 1)
xlabel('\mu');
ylabel('x');
title('Logistic Map - Bifurcation Diagram');
