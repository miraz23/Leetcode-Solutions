//Link: https://leetcode.com/problems/lru-cache/

class LRUCache {
private:
    unordered_map<int, int> key_value;
    unordered_map<int, list<int>::iterator> address;
    list<int>lruCache;
    int maxCapacity;

    void evict(){
        key_value.erase(lruCache.front());
        address.erase(lruCache.front());
        lruCache.pop_front();
    }
public:
    LRUCache(int capacity) {
        maxCapacity = capacity;
    }
    
    int get(int key) {
        if(!key_value.count(key)){
            return -1;
        }
        lruCache.erase(address[key]);
        lruCache.push_back(key);

        address[key] = (--lruCache.end()); 

        return key_value[key];
    }
    
    void put(int key, int value) {
        if(maxCapacity == lruCache.size() && !key_value.count(key)){
            evict();
        }

        if(key_value.count(key)){
            lruCache.erase(address[key]);
        }
        lruCache.push_back(key);
        address[key] = --lruCache.end();

        key_value[key] = value;
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */