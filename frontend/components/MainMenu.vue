<template>
  <div>
    <!-- Botão do menu -->
    <n-button
      circle
      class="fixed top-6 left-6 z-50 menu-btn !h-10 !w-10"
      @click="showDrawer = true"
    >
      <div class="i-carbon-menu text-xl" />
    </n-button>

    <!-- Drawer do menu -->
    <n-drawer
      v-model:show="showDrawer"
      :width="280"
      placement="left"
      class="main-drawer"
    >
      <n-drawer-content>
        <div class="flex flex-col h-full">
          <!-- Cabeçalho com perfil -->
          <div class="mb-8">
            <div class="flex items-center gap-3 mb-2">
              <div class="w-10 h-10 rounded-full bg-black/10 flex items-center justify-center">
                <div class="i-carbon-user text-xl text-black/70" />
              </div>
              <div>
                <div class="font-medium text-black/90">Usuário</div>
                <div class="text-xs text-black/60">usuario@email.com</div>
              </div>
            </div>
          </div>

          <!-- Menu principal -->
          <div class="flex-grow">
            <nav class="space-y-1">
              <!-- Link para nova nota -->
              <NuxtLink 
                to="/"
                class="flex items-center gap-3 p-3 rounded hover:bg-black/5 transition-colors text-black/90"
                active-class="bg-black/10 text-black font-medium"
                @click="showDrawer = false"
              >
                <div class="i-carbon-edit text-xl text-black/70" />
                <span>Nova Nota</span>
              </NuxtLink>

              <!-- Link para notas -->
              <NuxtLink 
                to="/notes"
                class="flex items-center gap-3 p-3 rounded hover:bg-black/5 transition-colors text-black/90"
                active-class="bg-black/10 text-black font-medium"
                @click="showDrawer = false"
              >
                <div class="i-carbon-document text-xl text-black/70" />
                <span>Minhas Notas</span>
              </NuxtLink>
            </nav>
          </div>

          <!-- Menu inferior -->
          <div class="mt-4">
            <div class="h-px bg-black/10" />
            <nav class="space-y-1 mt-4">
              <!-- Link para configurações -->
              <NuxtLink 
                to="/settings"
                class="flex items-center gap-3 p-3 rounded hover:bg-black/5 transition-colors text-sm text-black/80"
                active-class="bg-black/10 text-black font-medium"
                @click="showDrawer = false"
              >
                <div class="i-carbon-settings text-lg text-black/70" />
                <span>Configurações</span>
              </NuxtLink>

              <!-- Link para perfil -->
              <NuxtLink 
                to="/profile"
                class="flex items-center gap-3 p-3 rounded hover:bg-black/5 transition-colors text-sm text-black/80"
                active-class="bg-black/10 text-black font-medium"
                @click="showDrawer = false"
              >
                <div class="i-carbon-user-profile text-lg text-black/70" />
                <span>Perfil</span>
              </NuxtLink>
            </nav>
          </div>
        </div>
      </n-drawer-content>
    </n-drawer>
  </div>
</template>

<script setup lang="ts">
const showDrawer = ref(false)
</script>

<style>
.main-drawer .n-drawer-content {
  background: rgba(255, 255, 255, 0.97) !important;
  backdrop-filter: blur(12px);
}

.menu-btn {
  background: rgba(0, 0, 0, 0.9) !important;
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  transition: all 0.3s ease !important;
  color: white !important;
}

.menu-btn:hover {
  background: black !important;
  transform: translateY(-1px);
}

/* Remove cor azul do link ativo */
.router-link-active {
  color: black !important;
}
</style>
