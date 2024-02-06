<template>
  <div class="">
      <!-- Sidebar starts -->
      <!-- Remove class [ hidden ] and replace [ sm:flex ] with [ flex ] -->
      <div class="w-56 absolute sm:relative bg-blue-950 shadow md:h-full flex-col justify-between hidden sm:flex ">
          <div class="px-8">
              <div class="h-16 w-full flex items-center">
                <svg class="feather feather-user" fill="white" height="56" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
              <span class="text-white p-2">MCE - AP</span>
            </div>
              <ul class="mt-12">
                  <li class="flex w-full justify-between text-gray-300 hover:text-white cursor-pointer items-center mb-6">
                      <div class="flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-grid" width="18" height="18" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z"></path>
                              <rect x="4" y="4" width="6" height="6" rx="1"></rect>
                              <rect x="14" y="4" width="6" height="6" rx="1"></rect>
                              <rect x="4" y="14" width="6" height="6" rx="1"></rect>
                              <rect x="14" y="14" width="6" height="6" rx="1"></rect>
                          </svg>
                          <RouterLink to="/" class="text-sm ml-2">Dashboard</RouterLink>
                      </div>
                      <!-- <div class="py-1 px-3 bg-gray-700 rounded text-white flex items-center justify-center text-xs">5</div> -->
                  </li>
                  <li class="flex w-full justify-between text-gray-600 hover:text-white cursor-pointer items-center mb-6">
                      <div class="flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-puzzle" width="18" height="18" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z"></path>
                              <path d="M4 7h3a1 1 0 0 0 1 -1v-1a2 2 0 0 1 4 0v1a1 1 0 0 0 1 1h3a1 1 0 0 1 1 1v3a1 1 0 0 0 1 1h1a2 2 0 0 1 0 4h-1a1 1 0 0 0 -1 1v3a1 1 0 0 1 -1 1h-3a1 1 0 0 1 -1 -1v-1a2 2 0 0 0 -4 0v1a1 1 0 0 1 -1 1h-3a1 1 0 0 1 -1 -1v-3a1 1 0 0 1 1 -1h1a2 2 0 0 0 0 -4h-1a1 1 0 0 1 -1 -1v-3a1 1 0 0 1 1 -1"></path>
                          </svg>
                          <RouterLink to="/ordini" class="text-sm ml-2">Ordini</RouterLink>
                      
                      </div>
                      <!-- <div class="py-1 px-3 bg-gray-700 rounded text-white flex items-center justify-center text-xs">8</div> -->
                  </li>
                  <li class="flex w-full justify-between text-gray-600 hover:text-white cursor-pointer items-center mb-6">
                      <div class="flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-compass" width="18" height="18" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z"></path>
                              <polyline points="8 16 10 10 16 8 14 14 8 16"></polyline>
                              <circle cx="12" cy="12" r="9"></circle>
                          </svg>
                          <RouterLink to="/boards" class="text-sm ml-2">Schede</RouterLink>
                      </div>
                  </li>
                  <li class="flex w-full justify-between text-gray-600 hover:text-white cursor-pointer items-center mb-6">
                      <div class="flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-compass" width="18" height="18" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z"></path>
                              <polyline points="8 16 10 10 16 8 14 14 8 16"></polyline>
                              <circle cx="12" cy="12" r="9"></circle>
                          </svg>
                          <RouterLink to="/shipping" class="text-sm ml-2">Spedizioni</RouterLink>
                      </div>
                  </li>
                  <li class="flex w-full justify-between text-gray-600 hover:text-white cursor-pointer items-center mb-6">
                      <div class="flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-code" width="20" height="20" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z"></path>
                              <polyline points="7 8 3 12 7 16"></polyline>
                              <polyline points="17 8 21 12 17 16"></polyline>
                              <line x1="14" y1="4" x2="10" y2="20"></line>
                          </svg>
                          <RouterLink to="/tools/" class="text-sm ml-2">Tools</RouterLink>
                      </div>
                  </li>
                  <li class="flex w-full justify-between text-gray-600 hover:text-white cursor-pointer items-center mb-6">
                      <div class="flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-puzzle" width="18" height="18" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z"></path>
                              <path d="M4 7h3a1 1 0 0 0 1 -1v-1a2 2 0 0 1 4 0v1a1 1 0 0 0 1 1h3a1 1 0 0 1 1 1v3a1 1 0 0 0 1 1h1a2 2 0 0 1 0 4h-1a1 1 0 0 0 -1 1v3a1 1 0 0 1 -1 1h-3a1 1 0 0 1 -1 -1v-1a2 2 0 0 0 -4 0v1a1 1 0 0 1 -1 1h-3a1 1 0 0 1 -1 -1v-3a1 1 0 0 1 1 -1h1a2 2 0 0 0 0 -4h-1a1 1 0 0 1 -1 -1v-3a1 1 0 0 1 1 -1"></path>
                          </svg>
                          <RouterLink to="/stats/" class="text-sm ml-2">Statistiche</RouterLink>
                      </div>
                     
                  </li>
                  <!-- <li class="flex w-full justify-between text-gray-600 hover:text-white cursor-pointer items-center mb-6">
                      <div class="flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-stack" width="18" height="18" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z" />
                              <polyline points="12 4 4 8 12 12 20 8 12 4" />
                              <polyline points="4 12 12 16 20 12" />
                              <polyline points="4 16 12 20 20 16" />
                          </svg>
                          <span class="text-sm ml-2">Inventory</span>
                      </div>
                  </li>
                  <li class="flex w-full justify-between text-gray-600 hover:text-white cursor-pointer items-center">
                      <div class="flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-settings" width="18" height="18" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z" />
                              <path d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 0 0 -1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 0 0 -2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 0 0 -2.573 -1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                              <circle cx="12" cy="12" r="3" />
                          </svg>
                          <span class="text-sm ml-2">Settings</span>
                      </div> 
                  </li> -->
              </ul>
              <div class="flex justify-center mt-48 mb-4 w-full">
                  <!-- <div class="relative">
                      <div class="text-white absolute ml-4 inset-0 m-auto w-4 h-4">
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-search" width="16" height="16" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z"></path>
                              <circle cx="10" cy="10" r="7"></circle>
                              <line x1="21" y1="21" x2="15" y2="15"></line>
                          </svg>
                      </div>
                      <input class="bg-gray-700 focus:outline-none rounded w-full text-sm text-white pl-10 py-2" type="text" placeholder="Search" />
                  </div> -->
              </div>
          </div>
          <div class="px-8 border-t border-gray-700">
              <ul class="w-full flex items-center justify-between bg-blue-950">
                  <li class="cursor-pointer text-white pt-5 pb-3">
                  
                      <a class="btn btn-outline-secondary" href="/accounts/logout/">
                        Logout
                        </a>
                  </li>
                  <li class="cursor-pointer text-white pt-5 pb-3">
                  
                  <a class="btn btn-outline-secondary" href="/accounts/login/">
                    Login
                    </a>
              </li>
                  <li class="cursor-pointer text-white pt-5 pb-3">
                      <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-messages" width="20" height="20" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                          <path stroke="none" d="M0 0h24v24H0z"></path>
                          <path d="M21 14l-3 -3h-7a1 1 0 0 1 -1 -1v-6a1 1 0 0 1 1 -1h9a1 1 0 0 1 1 1v10"></path>
                          <path d="M14 15v2a1 1 0 0 1 -1 1h-7l-3 3v-10a1 1 0 0 1 1 -1h2"></path>
                      </svg>
                  </li>
                  <li class="cursor-pointer text-white pt-5 pb-3">
                      <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-settings" width="20" height="20" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                          <path stroke="none" d="M0 0h24v24H0z"></path>
                          <path d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 0 0 -1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 0 0 -2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 0 0 -2.573 -1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"></path>
                          <circle cx="12" cy="12" r="3"></circle>
                      </svg>
                  </li>
                  <li class="cursor-pointer text-white pt-5 pb-3">
                      <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-archive" width="20" height="20" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                          <path stroke="none" d="M0 0h24v24H0z"></path>
                          <rect x="3" y="4" width="18" height="4" rx="2"></rect>
                          <path d="M5 8v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-10"></path>
                          <line x1="10" y1="12" x2="14" y2="12"></line>
                      </svg>
                  </li>
              </ul>
          </div>
      </div>
      <div class="w-64 z-40 absolute bg-blue-950 shadow md:h-full flex-col justify-between sm:hidden transition duration-150 ease-in-out" id="mobile-nav">
          <div id="openSideBar" class="h-10 w-10 bg-blue-950 absolute right-0 mt-16 -mr-10 flex items-center shadow rounded-tr rounded-br justify-center cursor-pointer" @click="sidebarHandler(true)">
              <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-adjustments" width="20" height="20" viewBox="0 0 24 24" stroke-width="1.5" stroke="#FFFFFF" fill="none" stroke-linecap="round" stroke-linejoin="round">
                  <path stroke="none" d="M0 0h24v24H0z" />
                  <circle cx="6" cy="10" r="2" />
                  <line x1="6" y1="4" x2="6" y2="8" />
                  <line x1="6" y1="12" x2="6" y2="20" />
                  <circle cx="12" cy="16" r="2" />
                  <line x1="12" y1="4" x2="12" y2="14" />
                  <line x1="12" y1="18" x2="12" y2="20" />
                  <circle cx="18" cy="7" r="2" />
                  <line x1="18" y1="4" x2="18" y2="5" />
                  <line x1="18" y1="9" x2="18" y2="20" />
              </svg>
          </div>
          <div id="closeSideBar" class="h-10 w-10 bg-blue-950 absolute right-0 mt-16 -mr-10 flex items-center shadow rounded-tr rounded-br justify-center cursor-pointer text-white" @click="sidebarHandler(false)">
            <div v-if="!moved">
                <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-x" width="20" height="20" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                  <path stroke="none" d="M0 0h24v24H0z" />
                  <line x1="18" y1="6" x2="6" y2="18" />
                  <line x1="6" y1="6" x2="18" y2="18" />
              </svg>
            </div>
            <div v-else>
                <svg width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" fill="white">
                <path fill="#fff" fill-rule="evenodd" d="M19 4a1 1 0 01-1 1H2a1 1 0 010-2h16a1 1 0 011 1zm0 6a1 1 0 01-1 1H2a1 1 0 110-2h16a1 1 0 011 1zm-1 7a1 1 0 100-2H2a1 1 0 100 2h16z"/>
                </svg>
            </div>
            
          </div>
          <div class="px-8">
              <div class="h-16 w-full flex items-center">
                <H4 class="text-white">MCE APP</H4>
              </div>
              <ul class="mt-12">
                  <li class="flex w-full justify-between text-gray-300 hover:text-white cursor-pointer items-center mb-6">
                      <div class="flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-grid" width="18" height="18" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z"></path>
                              <rect x="4" y="4" width="6" height="6" rx="1"></rect>
                              <rect x="14" y="4" width="6" height="6" rx="1"></rect>
                              <rect x="4" y="14" width="6" height="6" rx="1"></rect>
                              <rect x="14" y="14" width="6" height="6" rx="1"></rect>
                          </svg>
                          <span class="text-sm ml-2">Dashboard</span>
                      </div>
                      <div class="py-1 px-3 bg-gray-700 rounded text-white flex items-center justify-center text-xs">5</div>
                  </li>
                  <li class="flex w-full justify-between text-gray-600 hover:text-white cursor-pointer items-center mb-6">
                      <div class="flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-puzzle" width="18" height="18" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z"></path>
                              <path d="M4 7h3a1 1 0 0 0 1 -1v-1a2 2 0 0 1 4 0v1a1 1 0 0 0 1 1h3a1 1 0 0 1 1 1v3a1 1 0 0 0 1 1h1a2 2 0 0 1 0 4h-1a1 1 0 0 0 -1 1v3a1 1 0 0 1 -1 1h-3a1 1 0 0 1 -1 -1v-1a2 2 0 0 0 -4 0v1a1 1 0 0 1 -1 1h-3a1 1 0 0 1 -1 -1v-3a1 1 0 0 1 1 -1h1a2 2 0 0 0 0 -4h-1a1 1 0 0 1 -1 -1v-3a1 1 0 0 1 1 -1"></path>
                          </svg>
                          <span class="text-sm ml-2">Ordini</span>
                      </div>
                      <div class="py-1 px-3 bg-gray-700 rounded text-white flex items-center justify-center text-xs">8</div>
                  </li>
                  <li class="flex w-full justify-between text-gray-600 hover:text-white cursor-pointer items-center mb-6">
                      <div class="flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-compass" width="18" height="18" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z"></path>
                              <polyline points="8 16 10 10 16 8 14 14 8 16"></polyline>
                              <circle cx="12" cy="12" r="9"></circle>
                          </svg>
                          <span class="text-sm ml-2">Schede</span>
                      </div>
                  </li>
                  <li class="flex w-full justify-between text-gray-600 hover:text-white cursor-pointer items-center mb-6">
                      <div class="flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-code" width="20" height="20" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z"></path>
                              <polyline points="7 8 3 12 7 16"></polyline>
                              <polyline points="17 8 21 12 17 16"></polyline>
                              <line x1="14" y1="4" x2="10" y2="20"></line>
                          </svg>
                          <span class="text-sm ml-2">Tools</span>
                      </div>
                  </li>
                  <!-- <li class="flex w-full justify-between text-gray-600 hover:text-white cursor-pointer items-center mb-6">
                      <div class="flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-puzzle" width="18" height="18" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z"></path>
                              <path d="M4 7h3a1 1 0 0 0 1 -1v-1a2 2 0 0 1 4 0v1a1 1 0 0 0 1 1h3a1 1 0 0 1 1 1v3a1 1 0 0 0 1 1h1a2 2 0 0 1 0 4h-1a1 1 0 0 0 -1 1v3a1 1 0 0 1 -1 1h-3a1 1 0 0 1 -1 -1v-1a2 2 0 0 0 -4 0v1a1 1 0 0 1 -1 1h-3a1 1 0 0 1 -1 -1v-3a1 1 0 0 1 1 -1h1a2 2 0 0 0 0 -4h-1a1 1 0 0 1 -1 -1v-3a1 1 0 0 1 1 -1"></path>
                          </svg>
                          <span class="text-sm ml-2">Processi</span>
                      </div>
                      <div class="py-1 px-3 bg-gray-700 rounded text-white flex items-center justify-center text-xs">25</div>
                  </li>
                  <li class="flex w-full justify-between text-gray-600 hover:text-white cursor-pointer items-center mb-6">
                      <div class="flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-stack" width="18" height="18" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z" />
                              <polyline points="12 4 4 8 12 12 20 8 12 4" />
                              <polyline points="4 12 12 16 20 12" />
                              <polyline points="4 16 12 20 20 16" />
                          </svg>
                          <span class="text-sm ml-2">Inventory</span>
                      </div>
                  </li>
                  <li class="flex w-full justify-between text-gray-600 hover:text-white cursor-pointer items-center">
                      <div class="flex items-center">
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-settings" width="18" height="18" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z" />
                              <path d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 0 0 2.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 0 0 1.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 0 0 -1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 0 0 -2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 0 0 -2.573 -1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 0 0 -1.065 -2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 0 0 1.066 -2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                              <circle cx="12" cy="12" r="3" />
                          </svg>
                          <span class="text-sm ml-2">Settings</span>
                      </div>
                  </li> -->
              </ul>
              <div class="flex justify-center mt-48 mb-4 w-full">
                  <div class="relative">
                      <!-- <div class="text-white absolute ml-4 inset-0 m-auto w-4 h-4">
                          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-search" width="16" height="16" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                              <path stroke="none" d="M0 0h24v24H0z"></path>
                              <circle cx="10" cy="10" r="7"></circle>
                              <line x1="21" y1="21" x2="15" y2="15"></line>
                          </svg>
                      </div>
                      <input class="focus:outline-none rounded w-full text-sm text-white bg-gray-100 pl-10 py-2" type="text" placeholder="Search" /> -->
                  </div>
              </div>
          </div>
         
      </div>
      <!-- Sidebar ends -->
    
  </div>
</template>

<script>
export default {
  name: "NavBar",
  data() {
      return {
          moved: true,
      };
  },
  methods: {
      sidebarHandler() {
          let sideBar = document.getElementById("mobile-nav");
          sideBar.style.transform = "translateX(-260px)";
          if (this.moved) {
              sideBar.style.transform = "translateX(0px)";
              this.moved = false;
          } else {
              sideBar.style.transform = "translateX(-260px)";
              this.moved = true;
          }
      },
  },
};
</script>
<script setup>
import { ref } from "vue";

const sidebarHandler = ()

</script>





 