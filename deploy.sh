aws s3 sync dist/wedding-website-angular/ s3://wedding-website-ui-content-s3 --delete
aws cloudfront create-invalidation --distribution-id=E13970GN2J3XOA --path=/*