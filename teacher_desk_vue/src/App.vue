<template>
  <div id="wrapper">
    <div class="margin-center">
      <nav class="navbar is-white mt-5 is-spaced">
        <div class="navbar-brand">
          <router-link to="/" class="navbar-item">
            <img src="./assets/brand-cropped.svg" width="180" />
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
            <router-link to="/about" class="navbar-item heading is-4 px-5">소개</router-link>
            <router-link to="/worksheet" class="navbar-item heading is-4 px-5">활동지 만들기</router-link>
            <router-link to="/blog" class="navbar-item heading is-4 px-5">블로그</router-link>
            <router-link to="/suggestions" class="navbar-item heading is-4 px-5">건의사항</router-link>
          </div>

        </div>
      </nav>
      <router-view />
    </div>
    <!-- <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2022</p>
    </footer> -->
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
// @import "../node_modules/bulma";
@import "../css/my-bulma.css";

@import "../css/mystyle.css";
</style>
