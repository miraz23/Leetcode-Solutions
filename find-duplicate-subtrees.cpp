/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    vector<TreeNode*> duplicateSubtrees;
    map<string, int> subtreeFrequency;
    string findDuplicate(TreeNode* currentNode){
        if(currentNode == NULL){
            return "";
        }
        string leftSubtree = findDuplicate(currentNode -> left);
        string rightSubtree = findDuplicate(currentNode -> right);
        string currentSubtree = to_string(currentNode -> val) + "#" + leftSubtree + "#" + rightSubtree;

        subtreeFrequency[currentSubtree]++;

        if(subtreeFrequency[currentSubtree] == 2){
            duplicateSubtrees.push_back(currentNode);
        }
        return currentSubtree;
    }
public:
    vector<TreeNode*> findDuplicateSubtrees(TreeNode* root) {
        findDuplicate(root);
        return duplicateSubtrees;
    }
};