<template>
  <div class="min-h-screen flex flex-col relative px-4 md:px-0">
    <div class="w-full max-w-3xl mx-auto flex-grow pt-24">
      <h1 class="text-2xl font-medium mb-8 text-black/90">Perfil</h1>
      
      <!-- Perfil -->
      <div class="space-y-8">
        <!-- Foto e nome -->
        <div class="flex items-center gap-6">
          <div class="w-20 h-20 rounded-full bg-black/10 flex items-center justify-center">
            <div class="i-carbon-user text-3xl text-black/70" />
          </div>
          <div>
            <div class="font-medium text-lg text-black/90">Usuário</div>
            <div class="text-black/60">usuario@email.com</div>
          </div>
        </div>

        <!-- Formulário -->
        <n-form class="text-black/90">
          <n-form-item label="Nome">
            <n-input v-model:value="profile.name" />
          </n-form-item>

          <n-form-item label="Email">
            <n-input v-model:value="profile.email" />
          </n-form-item>

          <n-form-item label="Bio">
            <n-input
              v-model:value="profile.bio"
              type="textarea"
              :autosize="{ minRows: 3, maxRows: 5 }"
            />
          </n-form-item>

          <div class="mt-8">
            <n-button type="primary" @click="saveProfile" class="bg-black text-white hover:bg-black/90">
              Salvar Alterações
            </n-button>
          </div>
        </n-form>

        <!-- Zona de perigo -->
        <section class="pt-8">
          <h2 class="text-lg font-medium mb-4 text-black/90">Zona de Perigo</h2>
          <n-button type="error" @click="confirmDeleteAccount" ghost>
            Excluir Conta
          </n-button>
        </section>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const profile = ref({
  name: 'Usuário',
  email: 'usuario@email.com',
  bio: ''
})

function saveProfile() {
  // TODO: Integrar com backend
  console.log('Saving profile:', profile.value)
}

function confirmDeleteAccount() {
  // TODO: Implementar confirmação e exclusão
  console.log('Confirming account deletion')
}
</script>

<style>
:deep(.n-button) {
  border-radius: 6px !important;
}
</style>
