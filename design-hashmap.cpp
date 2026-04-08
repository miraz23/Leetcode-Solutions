class MyHashMap {
private:
    const static int BUCKET_SIZE = 10004;
    const static int BASE = 991;
    const static int INVALID = -1;

    vector<pair<int, int>>keyValueMap[BUCKET_SIZE];

    int getHash(int key){
        int hashValue = (key * BASE) % BUCKET_SIZE;
        // cout << hashValue << endl;
        return hashValue;
    }

    bool isKeyExists(int key, int value){
        int hashValue = getHash(key);
        for(auto& kvp: keyValueMap[hashValue]){
            if(key == kvp.first){
                kvp.second = value;
                return true;
            }
        }
        return false;
    }
public:
    MyHashMap() {
        for(int i = 0; i < BUCKET_SIZE; i++){
            keyValueMap[i].clear();
        }
    }
    
    void put(int key, int value) {
        int hashValue = getHash(key);
        if(!isKeyExists(key, value)){
            keyValueMap[hashValue].push_back({key, value});
        }
    }
    
    int get(int key) {
        int hashValue = getHash(key);
        for(auto& kvp: keyValueMap[hashValue]){
            if(key == kvp.first){
                return kvp.second;
            }
        }
        return INVALID;
    }
    
    void remove(int key) {
        int hashValue = getHash(key);
        for(auto& kvp: keyValueMap[hashValue]){
            if(key == kvp.first){
                swap(kvp, keyValueMap[hashValue].back());
                keyValueMap[hashValue].pop_back();
                break;
            }
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */