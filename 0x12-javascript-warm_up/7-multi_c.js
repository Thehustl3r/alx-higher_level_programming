#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
  process.exit(1);
}
if (parseInt(process.argv[2]) < 0) {
  process.exit(1);
}
for (let i = 0; i < parseInt(process.argv[2]); i++) {
  console.log('C is fun');
}
