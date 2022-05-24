<template>
  <div id="wrapper">
    <nav class="navbar is-white">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <img src="./assets/교사의책상.png" >
        </router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          
        </a>
      </div>
      
    </nav>
    <nav class="navbar is-white">
      
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-start">
          <router-link to="/" class="navbar-item">🏠홈</router-link>
          <router-link to="/wordsearch" class="navbar-item">📕낱말 찾기</router-link>
          <button v-on:click="isEnHidden = !isEnHidden">Hide the text below</button>
          <div class="is-align-items-center is-flex">
              <router-link to="/wordsearch/kr" class="navbar-item button is-small is-rounded is-primary"  v-if="!isKrHidden">한국어</router-link>
          </div>
          <div class="is-align-items-center is-flex">
            <router-link to="/wordsearch/en" class="navbar-item button is-small is-rounded is-primary"   v-if="!isEnHidden">Eng</router-link>
          </div>
          <router-link to="/otherpuzzle" class="navbar-item">다른 퍼즐</router-link>

         
        </div>
        <div class="navbar-end">
    

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light">로그인</router-link>
              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart</span>
              </router-link>
            </div>
          </div>
        </div>
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
export default{
  data(){
    return {
      showMobileMenu:false, 
      isKrHidden: false,
      isEnHidden: true,
    }
  }
  
}</script>

<style lang="scss">
@import "../node_modules/bulma";
</style>
