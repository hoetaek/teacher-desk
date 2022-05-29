<template>
  <div id="wrapper">
    <nav class="navbar is-white p-3 is-size-4">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <img src="./assets/logo.png" />
          교사의 책상
        </router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{ 'is-active': showMobileMenu }">
        <div class="navbar-end">
          <router-link to="/" class="navbar-item ">🏠홈</router-link>
          <router-link to="/wordsearch" class="navbar-item ">📕낱말 찾기</router-link>
          <button v-on:click="fetchData()">Hide the text below</button>
          <!-- <button><a href="http://127.0.0.1:8000/wordsearch/?difficulty=DIFFICULT&is_uppercase=false&is_hint_twist=false&words=word,hello&responseType=blob">Hide the text below</a></button> -->
          <div class="is-align-items-center is-flex">
            <router-link to="/wordsearch/kr" class="navbar-item button is-small is-rounded is-primary"
              v-if="!isKrHidden">한국어</router-link>
          </div>
          <div class="is-align-items-center is-flex">
            <router-link to="/wordsearch/en" class="navbar-item button is-small is-rounded is-primary"
              v-if="!isEnHidden">Eng</router-link>
          </div>
          <router-link to="/otherpuzzle" class="navbar-item">다른 퍼즐</router-link>
        </div>
        <!-- <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light"
                >로그인</router-link
              >
              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart</span>
              </router-link>
            </div>
          </div>
        </div> -->
      </div>
    </nav>

    <section>
      <router-view />
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2022</p>
    </footer>
  </div>
</template>

<script>
import axios from "axios";
import fileDownload from 'js-file-download';


export default {
  name: "TestVueExaxios",

  data() {
    return {};
  },

  mounted() { },

  methods: {

    fetchData: function () {
      var params = new URLSearchParams();

      let colors = ['red', 'green', 'blue'];
      for (const color of colors) {
        params.append("words", color);
      }

      params.append("difficulty", "EASY");
      params.append("is_uppercase", false);
      params.append("is_hint_twist", false);

      axios({
        method: "GET",
        url: "http://127.0.0.1:8000/wordsearch",
        params: params,
        responseType: "blob",
        config: {
          headers: {
            'Accept': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            'Access-Control-Allow-Origin': 'http://localhost:8080',
            'Content-Type': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
          }
        }
      }).then(function (response) {
        const contentDisposition = response.headers['content-disposition'];
        let fileName = 'unknown';
        if (contentDisposition && contentDisposition.indexOf('attachment') !== -1) {
          var filenameRegex = /filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/;
          var matches = filenameRegex.exec(contentDisposition);
          if (matches != null && matches[1]) {
            fileName = matches[1].replace(/['"]/g, '');
          }
        }
        fileDownload(response.data, fileName);
      });
    },
    // method
  },
};

// export default{
//   data(){
//     return {
//       showMobileMenu:false,
//       isKrHidden: false,
//       isEnHidden: true,
//     }
//   }

// }
</script>

<style lang="scss">
@import "../sass/mystyles";
</style>
