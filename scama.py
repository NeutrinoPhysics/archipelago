#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import division

import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import params

metaparams = {
	'figure size'	: params.fgz,
	'bins' 		: params.bins,
	'font size'	: params.fsz,
	'marker size'	: params.ms,
	'alpha' 	: params.alpha,
	'marker' 	: params.mkr,
	'color array' 	: params.colarr,
	'line color' 	: params.lcol
}

class scama(object):

	def __init__(self, data=None, fgz=None, bins=None, fsz=None, ms=None, alpha=None, mkr=None, colarr=None, lcol=None):

		# --- initiation
		self.fgz  	= fgz  	 if fgz 	else metaparams['figure size']
		self.bins 	= bins 	 if bins 	else metaparams['bins'] 
		self.fsz  	= fsz  	 if fsz 	else metaparams['font size']
		self.ms  	= ms  	 if ms 		else metaparams['marker size']
		self.alpha  	= alpha  if alpha 	else metaparams['alpha']
		self.mkr  	= mkr  	 if mkr 	else metaparams['marker']
		self.colarr 	= colarr if colarr 	else metaparams['color array']
		self.lcol  	= lcol   if lcol  	else metaparams['line color']

		# --- set up data
		data 		= data   if data 	else np.load('test/data.npy')
		self.mat 	= data[:,:-1] 		 # data matrix
		self.lbl 	= data[:,-1] 		 # labels array

		self.ns, self.nf = self.mat.shape

		self.labels 	= np.unique(self.lbl) # labels keys
		self.feat 	= np.arange(self.nf)  # features id

		self.draw_figure()

		return


	def draw_figure(self):

		v1, v2 	= np.meshgrid(self.feat, self.feat)
		nb = self.nf * v2 + v1 + 1
		hidx = np.diag(nb)
		trix = np.tril(nb,-1)
		sidx = trix[trix>0]

		def find_vars(axid, nb):

			u1, u2 = np.where(nb==axid)

			return u1, u2

		def setup_histo(axid, nb):

			global fig, plt

			v1, v2 = find_vars(axid=axid, nb=nb)
			ax = plt.subplot(self.nf, self.nf, axid)

			ax.spines["right"].set_color("none")
			ax.spines["left"].set_color("none")
			ax.spines["top"].set_color("none")
			ax.tick_params(labelbottom=False, bottom=True, direction='in')
			ax.yaxis.set_major_locator(ticker.NullLocator())
			ax.xaxis.set_label_position("top")

			for k in range(self.labels.size):
				this_c = self.mat[:,v1[0]][self.lbl==self.labels[k]]
				ax.hist(this_c, bins=self.bins, color=self.colarr[k], alpha=self.alpha, linewidth=1., histtype='step')
			ax.set_xlabel('C'+str(v1[0]), fontsize=self.fsz[0])
	
			if v1[0]==self.nf-1:
				ax.tick_params(labelbottom=True, bottom=True, direction='in')
				plt.xticks(rotation=-60)
			else:
				ax.tick_params(labelbottom=False, bottom=True, direction='in')
				ax.set_xticks([])
			
			return

		def setup_scatter(axid, nb):

			global fig, plt

			v1, v2 = find_vars(axid=axid, nb=nb)
			ax = plt.subplot(self.nf, self.nf, axid)

			ax.tick_params(labelbottom=False, labeltop=False, labelleft=False, labelright=False, top=True, bottom=True, left=True, right=True)
			if v1 == self.nf-1:
				ax.tick_params(labelbottom=True, labeltop=False, labelleft=False, labelright=False, top=True, bottom=True, left=True, right=True)
			if v2 == 0:
				ax.tick_params(labelbottom=False, labeltop=False, labelleft=True, labelright=False, top=True, bottom=True, left=True, right=True)
			if ((v1 == self.nf-1) and (v2 == 0)):
				ax.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False, top=True, bottom=True, left=True, right=True)

			for k in range(self.labels.size):
				this_x = self.mat[:,v2[0]][self.lbl==self.labels[k]]
				this_y = self.mat[:,v1[0]][self.lbl==self.labels[k]]
				ax.scatter(this_x, this_y, color=self.colarr[k], alpha=self.alpha, s=self.ms, marker=self.mkr)
			plt.xticks(rotation=-60)

			return

		global fig, plt
		fig = plt.figure(figsize=(self.fgz, self.fgz))
		plt.subplots_adjust(wspace=0., hspace=0.)
		for ak in hidx:
			setup_histo(axid=ak, nb=nb)
		for ak in sidx:
			setup_scatter(axid=ak, nb=nb)
		plt.show()

		return





