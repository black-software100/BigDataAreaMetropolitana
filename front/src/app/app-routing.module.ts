import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { HomePage } from './home/home.page';
import { SantafeComponent } from './santafe/santafe.component';
import { CaucasiaComponent } from './caucasia/caucasia.component';
import { BelloComponent } from './bello/bello.component';
import { BelmiraComponent } from './belmira/belmira.component';
import { MallarinoComponent } from './mallarino/mallarino.component';
import { CaramantaComponent } from './caramanta/caramanta.component';
import { IndexComponent } from './index/index.component';

const routes: Routes = [
  {path:'',redirectTo:'home/inicio',pathMatch:'full'},
  {path: 'home', component:HomePage, children:[
    {path:'inicio',component:IndexComponent},
    {path:'SantaFe',component:SantafeComponent},
    {path:'Caucacia',component:CaucasiaComponent},
    {path:'Bello',component:BelloComponent},
    {path:'Belmira',component:BelmiraComponent},
    {path:'Mallarino',component:MallarinoComponent},
    {path:'Caramanta',component:CaramantaComponent}
  ]},

];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
