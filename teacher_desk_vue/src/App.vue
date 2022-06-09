<template>
  <div id="wrapper">
    <div class="margin-center">
      <nav class="navbar is-white mt-5 is-spaced">
        <div class="navbar-brand">
          <router-link
            to="/"
            class="navbar-item"
          >
            <img
              src="./assets/brand-cropped.svg"
              width="180"
            />
          </router-link>

          <a
            class="navbar-burger"
            aria-label="menu"
            aria-expanded="false"
            data-target="navbar-menu"
            @click="showMobileMenu = !showMobileMenu"
          >
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>
        <div
          class="navbar-menu"
          id="navbar-menu"
          v-bind:class="{ 'is-active': showMobileMenu }"
        >
          <div class="navbar-end">
            <router-link
              to="/about"
              class="navbar-item heading is-4 px-5"
            >소개</router-link>
            <router-link
              to="/worksheet"
              class="navbar-item heading is-4 px-5"
            >활동지 만들기</router-link>
            <router-link
              to="/blog"
              class="navbar-item heading is-4 px-5"
            >블로그</router-link>
            <router-link
              to="/suggestions"
              class="navbar-item heading is-4 px-5"
            >건의사항</router-link>
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
export default {
  name: "TestVueExaxios",

  data() {
    return { showMobileMenu: false };
  },
  methods: {},
};
</script>

<style lang="scss">
@import "../css/mystyles.css";
</style>
