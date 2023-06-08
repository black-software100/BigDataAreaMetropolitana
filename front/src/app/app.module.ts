import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouteReuseStrategy } from '@angular/router';

import { IonicModule, IonicRouteStrategy } from '@ionic/angular';

import { AppComponent } from './app.component';
import { HomePage } from './home/home.page';
import { AppRoutingModule } from './app-routing.module';
import { SantafeComponent} from './santafe/santafe.component'
import { MallarinoComponent } from './mallarino/mallarino.component';
import { CaucasiaComponent } from './caucasia/caucasia.component';
import { CaramantaComponent } from './caramanta/caramanta.component';
import { BelmiraComponent } from './belmira/belmira.component';
import { BelloComponent } from './bello/bello.component';
import { IndexComponent } from './index/index.component';
import { FooterComponent } from './footer/footer.component';
@NgModule({
  declarations: [
    AppComponent,
    IndexComponent,
    HomePage,
    SantafeComponent,
    MallarinoComponent,
    CaramantaComponent,
    CaucasiaComponent,
    BelmiraComponent,
    BelloComponent,
    FooterComponent
  ],
  imports: [BrowserModule, IonicModule.forRoot(), AppRoutingModule],
  providers: [{ provide: RouteReuseStrategy, useClass: IonicRouteStrategy }],
  bootstrap: [AppComponent],
})
export class AppModule {}
