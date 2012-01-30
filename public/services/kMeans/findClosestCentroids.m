function idx = findClosestCentroids(X, centroids)
%FINDCLOSESTCENTROIDS computes the centroid memberships for every example
%   idx = FINDCLOSESTCENTROIDS (X, centroids) returns the closest centroids
%   in idx for a dataset X where each row is a single example. idx = m x 1 
%   vector of centroid assignments (i.e. each entry in range [1..K])
%

% Initialize values
K = size(centroids, 1);
idx = zeros(size(X, 1), 1);

% For each example in X, find its closest centroid
for i = 1:size(X, 1)
	distanceMatrix = repmat(X(i,:), K, 1) - centroids;
	
	%Sum of squares of elements along dimension 1 (column-wise sum of squares)
	d = sumsq(distanceMatrix');
	
	%idx(i) contains the index of the centroid closest to example i
	[minvalue, index] = min(d,[],2);
	idx(i) = index;
end

