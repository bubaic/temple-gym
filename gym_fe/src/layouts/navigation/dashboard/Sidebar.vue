<template>
  <div id="sideBar" class="sidebar">
    <div class="flex flex-col">
      <!-- sidebar toggle -->
      <div class="text-right hidden md:block mb-4">
        <button id="sideBarHideBtn">
          <i class="fad fa-times-circle"></i>
        </button>
      </div>
      <!-- end sidebar toggle -->

      <p class="sidebar__head">homes</p>
      <a href="./index.html" class="sidebar__link">
        <i class="fad fa-chart-pie text-xs mr-2"></i>
        Analytics dashboard
      </a>

      <a href="./index-1.html" class="sidebar__link">
        <i class="fad fa-shopping-cart text-xs mr-2"></i>
        ecommerce dashboard
      </a>

      <p class="sidebar__head">apps</p>
      <a href="#" class="sidebar__link">
        <i class="fad fa-envelope-open-text text-xs mr-2"></i>
        email
      </a>

      <!-- link -->
      <a href="#" class="sidebar__link">
        <i class="fad fa-comments text-xs mr-2"></i>
        chat
      </a>
      <!-- end link -->

      <!-- link -->
      <a href="#" class="sidebar__link">
        <i class="fad fa-shield-check text-xs mr-2"></i>
        todo
      </a>
      <!-- end link -->

      <a href="#" class="sidebar__link">
        <i class="fad fa-calendar-edit text-xs mr-2"></i>
        calendar
      </a>
      <!-- end link -->

      <!-- link -->
      <p class="sidebar__head">reports</p>
      <a href="#" class="sidebar__link">
        <i class="fad fa-file-invoice-dollar text-xs mr-2"></i>
        invoice
      </a>
      <!-- end link -->
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
@import "@/assets/styles/reusable";

@layer base {
  .sidebar {
    @extend %flexColumn, %trans;
    @apply relative flex-wrap w-52 flex-none p-5
      md:fixed md:top-0 md:z-30 md:h-screen md:shadow-xl
			border-r border-gray-300 bg-light-500;
    // md:-ml-64 ;

    &__head {
      @apply uppercase text-xs text-gray-600 mb-4
				font-poppins font-semibold tracking-wider;

      &:not(:first-child) {
        @apply mt-4;
      }
    }
    &__link {
      @extend %trans;
      @apply mb-2 capitalize font-medium text-sm
				text-blue-gray-700 hover:text-brand-primary;
    }
  }
}
</style>
