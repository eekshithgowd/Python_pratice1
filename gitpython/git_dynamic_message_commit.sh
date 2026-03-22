#!/bin/bash

echo "Enter commit message:"
read msg

echo "Adding changes..."
git add .
echo "Committing changes..."
git commit -m "$msg"
echo "Pushing to GitHub..."
git push

echo "Done ✅"