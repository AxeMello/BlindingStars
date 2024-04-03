import fetch from "node-fetch";

// GitHub repository details
const repoOwner = 'AxeMello';
const repoName = 'BlindingStars';
const filePath = 'script.js';

// Construct the URL to access the raw content
const rawUrl = `https://raw.githubusercontent.com/${repoOwner}/${repoName}/main/${filePath}`;

// Fetch the COCO dataset
fetch(rawUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error(`Failed to fetch COCO dataset: ${response.status} ${response.statusText}`);
    }
    return response.json(); // Assuming COCO dataset is in JSON format
  })
  .then(cocoData => {
    // Use the COCO dataset in your code
    console.log(cocoData);
  })
  .catch(error => {
    console.error('Error fetching COCO dataset:', error);
  });