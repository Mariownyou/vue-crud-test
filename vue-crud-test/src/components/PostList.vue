<template>
    <div class="posts">
        <Post v-for="(post, index) in posts" :key="index" :post="post" />
    </div>
</template>

<script>
import PostDataService from '../services/PostDataService'
import Post from './Post'

export default {
    name: "post-list",
    data() {
        return {
            posts: [],
        }
    },
    methods: {
        retrievePosts() {
            PostDataService.getAll()
                .then(response =>  {
                    this.posts = response.data
                    console.log(response.data)
                })
                .catch(e => {
                    console.log(e)
                })
        }
    },
    mounted() {
        this.retrievePosts()
    }, 
    components: {
        Post,
    }
}
</script>