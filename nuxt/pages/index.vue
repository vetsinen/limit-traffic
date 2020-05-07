<template>
  <div>
    <h1 class="title">nuxt01 - {{title}}</h1>
    <ul>
      <li v-for="user in users">{{user.name}}</li>
    </ul>
    <p>
      Вооружившись этими сведениями ,весьма противоречивыми, как полагается настоящим профессиональным сведениям), вы входите в магазин фотографических аппаратов и пробуете произвести внушительное впечатление на продавца
    </p>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    components: {},
    data: () => {
      return {title: 'World', users: []}
    },
    mounted() {
      //https://jsonplaceholder.typicode.com/users
      axios
        .get(`http://localhost:8000/api/?format=json`)
        .then((res) => (this.users = res.data));
    }
  }
</script>

<style>
</style>
