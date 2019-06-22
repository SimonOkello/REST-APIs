from flask_restful import Resource
from flask import make_response, request, jsonify
import datetime
import time


blog_list = []

class Blogs(Resource):
    """docstring for Blogs"""
    def post(self):
        """Creating a blog"""
        req = request.get_json()
        new = {
            "id":len(blog_list) + 1,
            "title": req['title'],
            "description": req['description'],
            "date": datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        }
        blog_list.append(new)
        return make_response(jsonify(
            {
                "message": "Created",
                "blog_id": new['id']
            }
        ),201)

    def get(self):
        """retrieving all blog posts"""
        return make_response(jsonify(
            {
                "message": "Ok",
                "blogs": blog_list

        }),200)

class SinglBlog(Resource):
    """docstring for SingleBlog"""
    def get(self, id):
        """get single blog"""
        for blog in blog_list:
            if blog['id'] == id:
                return make_response(jsonify(
                    {
                        "message": "Ok",
                        "blog": blog
                    }
                ), 200)
            return make_response(jsonify(
                {
                    "message": "Not Found"
                }
            ), 404)

    def delete(self, id):
        """delete a single blog post"""
        global blog_list
        blog_list = [blog for blog in blog_list if blog['id'] != id]
        return make_response(jsonify(
            {
                "message": "The blog with id {} is deleted".format(id)
            }
        ), 200)
    def put(self, id):
        """edit a blog post"""
        for blog in blog_list:
            if blog['id'] == id:
                req = request.get_json
                blog['title'] = req ['title'],
                blog['description'] = req['description'],
                blog['updated'] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                return make_response(jsonify(
                    {
                        "message": "Ok",
                        "blog": blog
                    }
                ), 200)
            updated_blog = {
                "id": id,
                "title": req['title'],
                "description": req['description'],
                "updated": datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            }
            blog_list.append(updated_blog)
            return make_response(jsonify(
                {
                    "message": "Ok",
                    "blog": blog
                }
            ), 201)