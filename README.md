# Jungol

Jungol Let's go

## templete

```typescript
import fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "/input.txt";
var input = fs.readFileSync(__dirname + filePath).toString();

export const solution = (stdinInput: string) => {
  const [a, b] = stdinInput
    .trim()
    .split(" ")
    .map(Number);

  console.log(a + b);
};

solution(input);
```