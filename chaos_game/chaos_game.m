% Chaos game.
% The basic idea of this code is to observe the emergence of fractals through chaos.
%
clear, clc;
% Define the coordinates of the vertices of an equilateral triangle of side length=1:
v1 = [0,0];	% This vertex is at the origin on the x-y plane.
v2 = [1,0];	% This vertex has coods x=1, y=0.
v3 = [abs((v1(1)-v2(1))/2), sqrt(power((v1(1)-v2(1)),2) - power((v1(1)-v2(1))/2,2))];	% This is the third vertex.

% Plot the vertices:
plot(v1(1),v1(2));
hold on; % I think this is a MATLAB specific piece of code. This keeps what I have plotted, and allows me to superimpose subsequent points on the graph.
plot(v2(1),v2(2));
hold on;
plot(v3(1),v3(2));
hold on;

N = 10^5;   % Number of points I will plot.

% Initial point inside the triangle.
p = zeros(2,2); % Initialize a 2x2 empty matrix.
p(1,1) = 0.5;
p(1,2) = 0.1;
% The basic idea is to randomly choose a point anywhere inside the triangle. I have chosen the coods of this point to be x=0.5, y=0.1. I could have asked the computer to generate a random point inside the triangle as well, but I just chose this point.
plot(p(1,1),p(1,2));	% Plot this initial point. Let me call this P1.

for ii=2:1:N
    toss = randi([1,3]); % I want the computer to randomly choose either vertex 1, 2, or 3.
    if (toss==1)	% If vertex 1 was chosen, the next point to be plotted (call this P2) should be the mid point of of line segment joining vertex 1 and point P1.
        p(2,1) = v1(1) + abs(p(1,1) - v1(1))/2;
        p(2,2) = v1(2) + abs(p(1,2) - v1(2))/2;
    elseif (toss==2)	% If vertex 2 was chosen, the next point to be plotted (call this P2) should be the mid point of of line segment joining vertex 2 and point P1.
        p(2,1) = v2(1) - abs(p(1,1) - v2(1))/2;
        p(2,2) = v2(2) + abs(p(1,2) - v2(2))/2;
    elseif (toss==3)	% If vertex 3 was chosen, the next point to be plotted (call this P2) should be the mid point of of line segment joining vertex 3 and point P1.
        p(2,1) = v3(1) - abs(p(1,1) - v3(1))/2;
        p(2,2) = v3(2) - abs(p(1,2) - v3(2))/2;
    end
    
    plot(p(2,1),p(2,2)); % Plot point P2.
    
    % P1 = P2:
    p(1,1) = p(2,1);
    p(1,2) = p(2,2);
    
    % Re-initialize P2 for next iteration:
    p(2,1) = 0;
    p(2,2) = 0;
    
end
hold off;
