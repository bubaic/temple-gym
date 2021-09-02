<template>
  <div class="team__member">
    <img :src="img" alt="" />
    <div class="desc">
      <p class="name">{{ name }}</p>
      <p class="role">{{ role }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: ["name", "role", "img"],
  setup: () => {},
};
</script>

<style lang="scss" scoped>
@import "@/assets/styles/reusable";

@layer base {
  .team__member {
    @extend %flexColumn;
    @apply w-full sm:w-48 h-auto p-6 z-1;

    img {
      @extend %trans;
      @apply w-32 h-32 rounded-full filter grayscale;
    }

    .desc {
      @extend %flexColumn;
      @apply text-sm pt-2 capitalize relative;

      .name {
        @apply text-light-200 font-bold;
      }
      .role {
        @extend %trans;
        @apply top-0 left-1/2 absolute w-max duration-500
          transform -translate-x-1/2 opacity-0 text-gray-100;
      }
    }

    &:hover {
      img {
        @apply grayscale-0 ring-2 ring-brand-secondary;
      }
      .role {
        @apply opacity-100 top-6;
      }
    }
  }
}
</style>
