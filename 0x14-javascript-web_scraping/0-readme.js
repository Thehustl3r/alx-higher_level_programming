#!/usr/bin/node
const fs = require('fs');

async function readFile (filePath) {
  try {
    const content = await fs.promises.readFile(filePath, 'utf-8');
    return content;
  } catch (error) {
    console.error(error);
  }
}

const main = async () => {
  const filePath = process.argv[2];
  const content = await readFile(filePath);

  if (content) {
    console.log(content);
  }
};
main();
