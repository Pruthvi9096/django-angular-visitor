import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { VisitListComponent } from './visit-list/visit-list.component';

const routes: Routes = [
  {path: '', component: VisitListComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
