<template>
  <div class="worksheet">
    <section class="section">
      <div class="mb-6">
        <div class="title is-size-3-desktop is-size-4-tablet is-size-6-mobile has-text-grey-light">아이들이 찾게 될
          낱말의 언어를 선택해주세요</div>
      </div>
      <div class="section columns is-flex">
        <div class="column has-text-centered">
          <button
            @click="$router.push('/wordsearch/kr')"
            class="button is-responsive is-size-1-desktop is-size-3-tablet is-size-6-mobile is-link"
          >
            한국어
          </button>
        </div>
        <div class="column has-text-centered">
          <button
            @click="$router.push('/wordsearch/en')"
            class="button is-responsive is-size-1-desktop is-size-3-tablet is-size-6-mobile is-info"
            tag="button"
          >
            English
          </button>
        </div>

      </div>
    </section>

  </div>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
button {
  border-radius: 20px;
}
</style>
