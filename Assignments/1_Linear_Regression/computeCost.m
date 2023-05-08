function J = computeCost(X, y, theta)
%COMPUTECOST Compute cost for linear regression
%   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta
%               You should set J to the cost.

%{
%% Initial Implementation
hx = zeros(1,m);
for i = 1 : m
    hx(i) = theta'*X(i,:)';
end

for i = 1 : m
    J = J+(hx(i)-y(i))*(hx(i)-y(i));
end
J = J/(2*m);
%}

%% Shortcut
hx = X*theta-y;
J = (hx'*hx)/(2*m);



% =========================================================================

end
