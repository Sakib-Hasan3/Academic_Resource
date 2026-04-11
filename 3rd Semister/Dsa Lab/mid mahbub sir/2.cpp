#include <bits/stdc++.h>
using namespace std;

void addNodeAndPrint(vector<vector<int>>& adjMatrix, int& numNodes) 
{
    numNodes++;
    
    for (size_t i = 0; i < adjMatrix.size(); i++) 
    {
        adjMatrix[i].push_back(0);
    }
    
    adjMatrix.push_back(vector<int>(numNodes, 0));

    cout << "Graph after adding an extra node:\n";
    for (const auto& row : adjMatrix) 
    {
        for (int weight : row) 
        {
            cout << weight << " ";
        }
        cout << "\n";
    }
}

void addEdges(vector<vector<int>>& adjMatrix, const vector<pair<int, pair<int, int>>>& edges) 
{
    for (const auto& edge : edges) 
    {
        int from = edge.first;
        int to = edge.second.first;
        int weight = edge.second.second;

        
        if (from < adjMatrix.size() && to < adjMatrix.size()) 
        {
            
            adjMatrix[from][to] += weight;
            adjMatrix[to][from] += weight;
        }
        else 
        {
            cout << "Invalid edge: " << from << " -> " << to << endl;
        }
    }
}

int main() 
{
    
    vector<vector<int>> adjMatrix = 
    {
        {7, 5, 0, 0},
        {7, 0, 0, 2},
        {0, 3, 0, 0},
        {4, 0, 1, 0}
    };

    int numNodes = adjMatrix.size();

    cout << "Initial graph:\n";
    for (const auto& row : adjMatrix) 
    {
        for (int weight : row) 
        {
            cout << weight << " ";
        }
        cout << "\n";
    }

    
    vector<pair<int, pair<int, int>>> edgesToAdd = {
        {0, {1, 3}}, 
        {1, {2, 4}}, 
        {2, {3, 5}}, 
        {0, {3, 2}}  
    };

    addEdges(adjMatrix, edgesToAdd);

    cout << "Graph after adding edges:\n";
    for (const auto& row : adjMatrix) 
    {
        for (int weight : row) 
        {
            cout << weight << " ";
        }
        cout << "\n";
    }

    addNodeAndPrint(adjMatrix, numNodes);

    return 0;
}
