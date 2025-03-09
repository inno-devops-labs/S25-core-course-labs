## <ins>Which language has been chosen</ins> 
**The application was developed in Go (Golang) for its robust standard library, native concurrency support, and built-in timezone handling capabilities.**

## <ins>How the Time is displayed</ins>
**Moscow time is displayed in a UTC+3 formatted string using Go’s time package, automatically adjusting for daylight saving time through the Europe/Moscow IANA timezone database**

## <ins>Testing</ins>
**Testing involves manual browser checks**

## <ins>Best Practices & Code Quality</ins>

✅ Followed:

- Error handling for timezone loading

- Minimal dependencies, thread-safe code

- Proper time formatting (RFC3339-inspired)

- Clear separation of handler logic


