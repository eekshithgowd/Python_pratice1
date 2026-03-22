#!/bin/bash

echo "Adding changes..."
git add .

echo "Committing changes..."
git commit -m "Auto commit"

echo "Pushing to GitHub..."
git push

echo "Done ✅"