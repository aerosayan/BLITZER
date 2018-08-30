/**
  * @brief : Floyd-Warshall algorithm
  * @cmplx : O(n^3) complexity in time ,n is the number of vertices
  * @info  : returns the shortest distance between every pair of vertices 
  *        : in an edge weighted directed graph.  
  **/
vec<vec<ll> > floyd_warshall(vec<vec<ll> > wgraph)
{
	// n is the number of vertices in the digraph
	ll n = wgraph.sz;

	// distance matrix
	// @note : initialized to size of weighted graph but set to infinity value
	// @note : oo is infinity
	vec<vec<ll> > dist(n,vec<ll>(n,INFL));

	// full fill the distance matrix from the graph
	// @cmplx : O(n) in time , instead of O(n^2) used for filling a matrix
	rep(szt,i,0,n)
		dist[i][i] = 0;

	// core floyd-warshall algorithm
	rep(szt,k,0,n)
		rep(szt,i,0,n)
			rep(szt,j,0,n)
				dist[i][j] = max(dist[i][j],dist[i][k]+dist[k][j]);

	// return the solution matrix
	return dist;
}

