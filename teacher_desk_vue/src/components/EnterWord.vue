<template>
  <div class="tile is-ancestor">
    <div class="tile is-parent">
      <article class="tile is-child notification has-background-grey-lighter is-rounded">
        <input
          class="input is-static center-block"
          type="text"
          placeholder="단어"
          v-model="text1"
          @input="onDataChanged"
          v-on:keypress="isValidateLetter($event)"
        />
      </article>
    </div>
    <div class="tile is-parent">
      <article class="tile is-child notification has-background-grey-lighter is-rounded">
        <input
          class="input is-static center-block"
          type="text"
          placeholder="단어"
          v-model="text2"
          @input="onDataChanged"
          v-on:keypress="isValidateLetter($event)"
        />
      </article>
    </div>
    <div class="tile is-parent">
      <article class="tile is-child notification has-background-grey-lighter is-rounded">
        <input
          class="input is-static center-block"
          type="text"
          placeholder="단어"
          v-model="text3"
          @input="onDataChanged"
          v-on:keypress="isValidateLetter($event)"
        />
      </article>
    </div>
    <div class="tile is-parent">
      <article class="tile is-child notification has-background-grey-lighter is-rounded">
        <input
          class="input is-static center-block"
          type="text"
          placeholder="단어"
          v-model="text4"
          @input="onDataChanged"
          v-on:keypress="isValidateLetter($event)"
        />
      </article>
    </div>
    <div class="tile is-parent">
      <article class="tile is-child notification has-background-grey-lighter is-rounded">
        <input
          class="input is-static center-block"
          type="text"
          placeholder="단어"
          v-model="text5"
          @input="onDataChanged"
          v-on:keypress="isValidateLetter($event)"
        />
      </article>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      text1: "",
      text2: "",
      text3: "",
      text4: "",
      text5: "",
    };
  },
  props: {
    validateRegex: RegExp,
  },
  methods: {
    onDataChanged() {
      this.$emit("textInputChanged", [
        this.text1,
        this.text2,
        this.text3,
        this.text4,
        this.text5,
      ]);
    },
    isValidateLetter(e) {
      let char = String.fromCharCode(e.keyCode);
      if (this.validateRegex.test(char)) return true;
      // if (/^[A-Za-z0-9]+$/.test(char)) return true;
      else e.preventDefault();
    },
  },
  emits: ["textInputChanged"],
};
</script>
