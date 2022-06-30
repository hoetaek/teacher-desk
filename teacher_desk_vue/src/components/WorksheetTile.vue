<template >
  <div>
    <div class="card">
      <div
        v-if="isNotReady"
        class="overlay title is-size-3 center"
      >업데이트 예정</div>
      <div class="container p-4">
        <div class="card-image">
          <figure class="image is-square">
            <img
              :src="require(`@/assets/${filename}`)"
              alt="Image"
            >
          </figure>
        </div>
      </div>
      <div class="card-content">

        <div class="content">
          <h1
            class="title has-text-left"
            @click="$router.push('/wordsearch')"
            @mouseover="isHover=true"
            @mouseleave="isHover=false"
            style="cursor: pointer"
            :class="classObject"
          >
            <slot name="title"></slot>
          </h1>
          <span class="subtitle is-4">
            <slot name="description"></slot>
          </span>
          <br>
          <div class="level">
            <div class="level-item level-right">
              <div class="icon is-medium">
                <div v-if="liked"><i class="fas fa-heart"></i></div>
                <div v-else>
                  <i class="far fa-heart"></i>
                </div>
              </div>
              <span>
                <slot name="heartNum"></slot>
              </span>

            </div>
          </div>

        </div>

      </div>

    </div>

  </div>
</template>
<script>
export default {
  data() {
    return {
      isHover: false,
    };
  },
  props: {
    filename: String,
    liked: Boolean,
    isNotReady: Boolean,
  },
  computed: {
    classObject: function () {
      return {
        "title size-is-3 has-text-centered": true,
        "has-text-link": this.isHover,
        "is-underlined": this.isHover,
      };
    },
  },
};
</script>

<style scoped>
.card {
  box-shadow: none;
  border: solid 3px;
  border-radius: 25px;
}
.icon {
  display: flex;
  justify-content: center;
  align-items: center;
}

.overlay {
  position: absolute;
  opacity: 0.8;
  background-color: #b8b8b8;
  width: 100%;
  height: 100%;
  border-radius: 20px;
  z-index: 3;
  color: black;
}
.center {
  display: flex;
  justify-content: center; /* align horizontal */
  align-items: center;
}
</style>