# Social Media API - Posts & Comments

## Endpoints

### Posts
- GET /posts/ → Get all posts (paginated)
- POST /posts/ → Create a post (Auth required)
- GET /posts/?search={query} → Filter posts by title/content

### Comments
- GET /posts/{post_id}/comments/ → Get all comments on a post
- POST /posts/{post_id}/comments/ → Add a comment (Auth required)

## Example: Creating a Post
Request:
```bash
curl -X POST -H "Authorization: Token YOUR_TOKEN" -H "Content-Type: application/json" -d '{"title": "New Post", "content": "This is my first post!"}' http://127.0.0.1:8000/posts/


---

### 🎯 **Final Deliverables**
✅ **Posts & Comments Models**  
✅ **Serializers for Posts & Comments**  
✅ **CRUD API Views**  
✅ **URL Configuration**  
✅ **Pagination & Filtering**  
✅ **Comprehensive API Documentation**  

