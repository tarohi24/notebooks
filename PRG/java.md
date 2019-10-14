Java
=========

## Multi threading

### Basic form
```java
Thread a = new Thread(new Runnable(){
     public void run(){
          # procedure
     }
}
```

### syncronized
`syncronized` gives a locking to a method (it allows to execute exclusively). It may harmful in terms of performance.


### volatile
To prevent from caching, `volatile` offers an useful function.:

```jaav
volatile private int a;
```

Caching is sometimes suffering from dirty-write interruption.

CAUTION: `volatile` does not guarantee a variable is atomic. For instance, in the following case, `nextSerialNumber` may has an unexpected value because `++` is not an atomic operation.

```java
private static volatile int nextSerialNumber = 0;

public static in generateSerialNumber() {
     return ++nextSerialNumber+
}
```
