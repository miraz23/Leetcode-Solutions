class MyCircularQueue {
private:
    int frontPointer;
    int queueCapacity;
    int queueSize;
    vector<int>queue;

    int findIndex(int currentIndex){
        if(currentIndex >= queueCapacity) return currentIndex - queueCapacity;
        else if(currentIndex < 0) return currentIndex + queueCapacity;

        return currentIndex;
    }
public:
    MyCircularQueue(int k) {
        frontPointer = 0;
        queue.assign(k, 0);
        queueCapacity = k;
        queueSize = 0;
    }
    
    bool enQueue(int value) {
        if(queueSize == queueCapacity)
            return false;

        queue[ findIndex(frontPointer+queueSize) ] = value;
        queueSize++;

        return true;
    }
    
    bool deQueue() {
        if(queueSize == 0)
            return false;

        frontPointer = findIndex(frontPointer + 1);
        queueSize--;

        return true;
    }
    
    int Front() {
        return queueSize == 0 ? -1 : queue[frontPointer];
    }
    
    int Rear() {
        return queueSize == 0 ? -1 : queue[ findIndex(frontPointer + queueSize - 1) ];
    }
    
    bool isEmpty() {
        return queueSize == 0;
    }
    
    bool isFull() {
        return queueSize == queueCapacity;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */