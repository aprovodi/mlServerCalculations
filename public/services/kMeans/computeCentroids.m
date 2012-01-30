function centroids = computeCentroids(X, idx, K)
%COMPUTECENTROIDS returs the new centroids by computing the means of the 
%data points assigned to each centroid.
%   centroids = COMPUTECENTROIDS(X, idx, K) returns the new centroids by 
%   computing the means of the data points assigned to each centroid. It is
%   given a dataset X where each row is a single data point, a vector
%   idx of centroid assignments (i.e. each entry in range [1..K]) for each
%   example, and K, the number of centroids. It returns a matrix
%   centroids, where each row of centroids is the mean of the data points
%   assigned to it.
%

% Initialize values
[m n] = size(X);
centroids = zeros(K, n);

% Go over every centroid and compute mean of all points that belong to it.
for i = 1:K
	centroids(i,:) = mean(X(idx == i,:), 1);
end

end

