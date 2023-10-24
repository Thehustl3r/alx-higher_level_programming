#!/usr/bin/node
const fs = require('fs');

async function writeStringToFile (filePath, str) {
  try {
    await fs.promises.writeFile(filePath, str, 'utf-8');
  } catch (error) {
    console.error(error);
  }
}

const main = async () => {
  const filePath = process.argv[2];
  const str = process.argv[3];

  await writeStringToFile(filePath, str);
};
main();
