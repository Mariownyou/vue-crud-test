<template>

  <form @submit.prevent="submit">
      <div class="field">
        <label class="label" for="title">Title</label>
        <input
          type="text"
          class="input"
          id="title"
          required
          v-model="post.title"
          name="title"
        />
      </div>

      <div class="field">
        <label class="label" for="text">Text</label>
        <textarea
          class="textarea"
          id="text"
          required
          v-model="post.text"
          name="text"
        />
      </div>

      <button type="submit" class="button is-success">Submit</button>
    </form>

</template>

<script>
export default {
    props: ['method', 'post'],
    methods: {
        submit() {
            const router = this.$router

            // Вызываем метод который получили из компонента
            this.method()

            // Перенаправляем пользователя на главную
            router.push({
                name: 'posts'
            })
        }
    }
}

</script>

<style>

</style>