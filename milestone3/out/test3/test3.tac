.str0: "mySudoku"
.str1: ""
.str2: "Solution found:"
.str3: "No solution exists."

Solution.__init__:
	beginfunc 0
	#t0 = self
	#t1 = #t0
	#t1 = 0 + #t1
	#t2 = .str0
	*(#t1) = #t2
	leave
	return  
	endfunc 


Solution.printGrid:
	beginfunc 16
	i = 0
	j = 0
	#t3 = i
	#t4 = 9
	i = 0
	#t5 = i
	jump L1

L0:
	#t5 = #t5 + 1
	i = #t5

L1:
	#t6 = #t5 < #t4
	ifFalse #t6 jump L5
	#t7 = j
	#t8 = 9
	j = 0
	#t9 = j
	jump L3

L2:
	#t9 = #t9 + 1
	j = #t9

L3:
	#t10 = #t9 < #t8
	ifFalse #t10 jump L4
	#t11 = arr
	#t12 = i
	#t13 = 8 * #t12
	#t13 = #t11 + #t13
	#t13 = 8 + #t13
	#t14 = *(#t13)
	#t15 = j
	#t16 = 8 * #t15
	#t16 = #t14 + #t16
	#t16 = 8 + #t16
	#t17 = *(#t16)
	save registers  
	stackpointer -8 
	param #t17 
	call print_int 1
	stackpointer +8 
	restore registers  
	jump L2

L4:
	#t18 = .str1
	save registers  
	stackpointer -8 
	param #t18 
	call print_str 1
	stackpointer +8 
	restore registers  
	jump L0

L5:
	leave
	return  
	endfunc 


Solution.used_in_row:
	beginfunc 8
	i = 0
	#t19 = i
	#t20 = 9
	i = 0
	#t21 = i
	jump L7

L6:
	#t21 = #t21 + 1
	i = #t21

L7:
	#t22 = #t21 < #t20
	ifFalse #t22 jump L9
	#t23 = arr
	#t24 = row
	#t25 = 8 * #t24
	#t25 = #t23 + #t25
	#t25 = 8 + #t25
	#t26 = *(#t25)
	#t27 = i
	#t28 = 8 * #t27
	#t28 = #t26 + #t28
	#t28 = 8 + #t28
	#t29 = *(#t28)
	#t30 = num
	#t29 = #t29 == #t30
	ifFalse #t29 jump L8
	#t31 = 1
	leave
	return #t31 
	jump L8

L8:
	jump L6

L9:
	#t32 = 0
	leave
	return #t32 
	endfunc 


Solution.used_in_col:
	beginfunc 8
	i = 0
	#t33 = i
	#t34 = 9
	i = 0
	#t35 = i
	jump L11

L10:
	#t35 = #t35 + 1
	i = #t35

L11:
	#t36 = #t35 < #t34
	ifFalse #t36 jump L13
	#t37 = arr
	#t38 = i
	#t39 = 8 * #t38
	#t39 = #t37 + #t39
	#t39 = 8 + #t39
	#t40 = *(#t39)
	#t41 = col
	#t42 = 8 * #t41
	#t42 = #t40 + #t42
	#t42 = 8 + #t42
	#t43 = *(#t42)
	#t44 = num
	#t43 = #t43 == #t44
	ifFalse #t43 jump L12
	#t45 = 1
	leave
	return #t45 
	jump L12

L12:
	jump L10

L13:
	#t46 = 0
	leave
	return #t46 
	endfunc 


Solution.used_in_box:
	beginfunc 16
	i = 0
	j = 0
	#t47 = i
	#t48 = 3
	i = 0
	#t49 = i
	jump L15

L14:
	#t49 = #t49 + 1
	i = #t49

L15:
	#t50 = #t49 < #t48
	ifFalse #t50 jump L20
	#t51 = j
	#t52 = 3
	j = 0
	#t53 = j
	jump L17

L16:
	#t53 = #t53 + 1
	j = #t53

L17:
	#t54 = #t53 < #t52
	ifFalse #t54 jump L19
	#t55 = arr
	#t56 = i
	#t57 = row
	#t56 = #t56 + #t57
	#t58 = 8 * #t56
	#t58 = #t55 + #t58
	#t58 = 8 + #t58
	#t59 = *(#t58)
	#t60 = j
	#t61 = col
	#t60 = #t60 + #t61
	#t62 = 8 * #t60
	#t62 = #t59 + #t62
	#t62 = 8 + #t62
	#t63 = *(#t62)
	#t64 = num
	#t63 = #t63 == #t64
	ifFalse #t63 jump L18
	#t65 = 1
	leave
	return #t65 
	jump L18

L18:
	jump L16

L19:
	jump L14

L20:
	#t66 = 0
	leave
	return #t66 
	endfunc 


Solution.check_location_is_safe:
	beginfunc 0
	#t67 = self
	#t68 = arr
	#t69 = row
	#t70 = num
	save registers  
	stackpointer -32 
	param #t70 
	param #t69 
	param #t68 
	param #t67 
	call Solution.used_in_row 4
	#t71 = return_value
	stackpointer +32 
	restore registers  
	#t71 =  ! #t71
	#t72 = self
	#t73 = arr
	#t74 = col
	#t75 = num
	save registers  
	stackpointer -32 
	param #t75 
	param #t74 
	param #t73 
	param #t72 
	call Solution.used_in_col 4
	#t76 = return_value
	stackpointer +32 
	restore registers  
	#t76 =  ! #t76
	#t71 = #t71 && #t76
	#t77 = self
	#t78 = arr
	#t79 = row
	#t80 = row
	#t81 = 3
	#t80 = #t80 % #t81
	#t79 = #t79 - #t80
	#t82 = col
	#t83 = col
	#t84 = 3
	#t83 = #t83 % #t84
	#t82 = #t82 - #t83
	#t85 = num
	save registers  
	stackpointer -40 
	param #t85 
	param #t82 
	param #t79 
	param #t78 
	param #t77 
	call Solution.used_in_box 5
	#t86 = return_value
	stackpointer +40 
	restore registers  
	#t86 =  ! #t86
	#t71 = #t71 && #t86
	leave
	return #t71 
	endfunc 


Solution.find_empty_location:
	beginfunc 16
	row = 0
	col = 0
	#t87 = row
	#t88 = 9
	row = 0
	#t89 = row
	jump L22

L21:
	#t89 = #t89 + 1
	row = #t89

L22:
	#t90 = #t89 < #t88
	ifFalse #t90 jump L27
	#t91 = col
	#t92 = 9
	col = 0
	#t93 = col
	jump L24

L23:
	#t93 = #t93 + 1
	col = #t93

L24:
	#t94 = #t93 < #t92
	ifFalse #t94 jump L26
	#t95 = arr
	#t96 = row
	#t97 = 8 * #t96
	#t97 = #t95 + #t97
	#t97 = 8 + #t97
	#t98 = *(#t97)
	#t99 = col
	#t100 = 8 * #t99
	#t100 = #t98 + #t100
	#t100 = 8 + #t100
	#t101 = *(#t100)
	#t102 = 0
	#t101 = #t101 == #t102
	ifFalse #t101 jump L25
	#t103 = l
	#t104 = 0
	#t105 = 8 * #t104
	#t105 = #t103 + #t105
	#t105 = 8 + #t105
	#t106 = *(#t105)
	#t107 = row
	*(#t105) = #t107
	#t108 = l
	#t109 = 1
	#t110 = 8 * #t109
	#t110 = #t108 + #t110
	#t110 = 8 + #t110
	#t111 = *(#t110)
	#t112 = col
	*(#t110) = #t112
	#t113 = 1
	leave
	return #t113 
	jump L25

L25:
	jump L23

L26:
	jump L21

L27:
	#t114 = 0
	leave
	return #t114 
	endfunc 


Solution.SolveSudoku:
	beginfunc 32
	#t115 = 0
	#t116 = 0
	#t117 = 24
	save registers  
	stackpointer -8 
	param #t117 
	call allocmem 1
	#t117 = return_value
	stackpointer +8 
	restore registers  
	#t118 = #t117
	*(#t118) = 2
	#t118 = 8 + #t118
	*(#t118) = #t115
	#t118 = 8 + #t118
	*(#t118) = #t116
	l = #t117
	#t119 = self
	#t120 = grid
	#t121 = l
	save registers  
	stackpointer -24 
	param #t121 
	param #t120 
	param #t119 
	call Solution.find_empty_location 3
	#t122 = return_value
	stackpointer +24 
	restore registers  
	#t122 =  ! #t122
	ifFalse #t122 jump L28
	#t123 = 1
	leave
	return #t123 
	jump L28

L28:
	#t124 = l
	#t125 = 0
	#t126 = 8 * #t125
	#t126 = #t124 + #t126
	#t126 = 8 + #t126
	#t127 = *(#t126)
	row = #t127
	#t128 = l
	#t129 = 1
	#t130 = 8 * #t129
	#t130 = #t128 + #t130
	#t130 = 8 + #t130
	#t131 = *(#t130)
	col = #t131
	num = 0
	#t132 = num
	#t133 = 1
	#t134 = 10
	num = #t133
	#t135 = num
	jump L30

L29:
	#t135 = #t135 + 1
	num = #t135

L30:
	#t136 = #t135 < #t134
	ifFalse #t136 jump L33
	#t137 = self
	#t138 = grid
	#t139 = row
	#t140 = col
	#t141 = num
	save registers  
	stackpointer -40 
	param #t141 
	param #t140 
	param #t139 
	param #t138 
	param #t137 
	call Solution.check_location_is_safe 5
	#t142 = return_value
	stackpointer +40 
	restore registers  
	ifFalse #t142 jump L32
	#t143 = grid
	#t144 = row
	#t145 = 8 * #t144
	#t145 = #t143 + #t145
	#t145 = 8 + #t145
	#t146 = *(#t145)
	#t147 = col
	#t148 = 8 * #t147
	#t148 = #t146 + #t148
	#t148 = 8 + #t148
	#t149 = *(#t148)
	#t150 = num
	*(#t148) = #t150
	#t151 = self
	#t152 = grid
	save registers  
	stackpointer -16 
	param #t152 
	param #t151 
	call Solution.SolveSudoku 2
	#t153 = return_value
	stackpointer +16 
	restore registers  
	ifFalse #t153 jump L31
	#t154 = 1
	leave
	return #t154 
	jump L31

L31:
	#t155 = grid
	#t156 = row
	#t157 = 8 * #t156
	#t157 = #t155 + #t157
	#t157 = 8 + #t157
	#t158 = *(#t157)
	#t159 = col
	#t160 = 8 * #t159
	#t160 = #t158 + #t160
	#t160 = 8 + #t160
	#t161 = *(#t160)
	#t162 = 0
	*(#t160) = #t162
	jump L32

L32:
	jump L29

L33:
	#t163 = 0
	leave
	return #t163 
	endfunc 


main:
	beginfunc 16
	#t164 = 3
	#t165 = 0
	#t166 = 6
	#t167 = 5
	#t168 = 0
	#t169 = 8
	#t170 = 4
	#t171 = 0
	#t172 = 0
	#t173 = 80
	save registers  
	stackpointer -8 
	param #t173 
	call allocmem 1
	#t173 = return_value
	stackpointer +8 
	restore registers  
	#t174 = #t173
	*(#t174) = 9
	#t174 = 8 + #t174
	*(#t174) = #t164
	#t174 = 8 + #t174
	*(#t174) = #t165
	#t174 = 8 + #t174
	*(#t174) = #t166
	#t174 = 8 + #t174
	*(#t174) = #t167
	#t174 = 8 + #t174
	*(#t174) = #t168
	#t174 = 8 + #t174
	*(#t174) = #t169
	#t174 = 8 + #t174
	*(#t174) = #t170
	#t174 = 8 + #t174
	*(#t174) = #t171
	#t174 = 8 + #t174
	*(#t174) = #t172
	#t175 = 5
	#t176 = 2
	#t177 = 0
	#t178 = 0
	#t179 = 0
	#t180 = 0
	#t181 = 0
	#t182 = 0
	#t183 = 0
	#t184 = 80
	save registers  
	stackpointer -8 
	param #t184 
	call allocmem 1
	#t184 = return_value
	stackpointer +8 
	restore registers  
	#t185 = #t184
	*(#t185) = 9
	#t185 = 8 + #t185
	*(#t185) = #t175
	#t185 = 8 + #t185
	*(#t185) = #t176
	#t185 = 8 + #t185
	*(#t185) = #t177
	#t185 = 8 + #t185
	*(#t185) = #t178
	#t185 = 8 + #t185
	*(#t185) = #t179
	#t185 = 8 + #t185
	*(#t185) = #t180
	#t185 = 8 + #t185
	*(#t185) = #t181
	#t185 = 8 + #t185
	*(#t185) = #t182
	#t185 = 8 + #t185
	*(#t185) = #t183
	#t186 = 0
	#t187 = 8
	#t188 = 7
	#t189 = 0
	#t190 = 0
	#t191 = 0
	#t192 = 0
	#t193 = 3
	#t194 = 1
	#t195 = 80
	save registers  
	stackpointer -8 
	param #t195 
	call allocmem 1
	#t195 = return_value
	stackpointer +8 
	restore registers  
	#t196 = #t195
	*(#t196) = 9
	#t196 = 8 + #t196
	*(#t196) = #t186
	#t196 = 8 + #t196
	*(#t196) = #t187
	#t196 = 8 + #t196
	*(#t196) = #t188
	#t196 = 8 + #t196
	*(#t196) = #t189
	#t196 = 8 + #t196
	*(#t196) = #t190
	#t196 = 8 + #t196
	*(#t196) = #t191
	#t196 = 8 + #t196
	*(#t196) = #t192
	#t196 = 8 + #t196
	*(#t196) = #t193
	#t196 = 8 + #t196
	*(#t196) = #t194
	#t197 = 0
	#t198 = 0
	#t199 = 3
	#t200 = 0
	#t201 = 1
	#t202 = 0
	#t203 = 0
	#t204 = 8
	#t205 = 0
	#t206 = 80
	save registers  
	stackpointer -8 
	param #t206 
	call allocmem 1
	#t206 = return_value
	stackpointer +8 
	restore registers  
	#t207 = #t206
	*(#t207) = 9
	#t207 = 8 + #t207
	*(#t207) = #t197
	#t207 = 8 + #t207
	*(#t207) = #t198
	#t207 = 8 + #t207
	*(#t207) = #t199
	#t207 = 8 + #t207
	*(#t207) = #t200
	#t207 = 8 + #t207
	*(#t207) = #t201
	#t207 = 8 + #t207
	*(#t207) = #t202
	#t207 = 8 + #t207
	*(#t207) = #t203
	#t207 = 8 + #t207
	*(#t207) = #t204
	#t207 = 8 + #t207
	*(#t207) = #t205
	#t208 = 9
	#t209 = 0
	#t210 = 0
	#t211 = 8
	#t212 = 6
	#t213 = 3
	#t214 = 0
	#t215 = 0
	#t216 = 5
	#t217 = 80
	save registers  
	stackpointer -8 
	param #t217 
	call allocmem 1
	#t217 = return_value
	stackpointer +8 
	restore registers  
	#t218 = #t217
	*(#t218) = 9
	#t218 = 8 + #t218
	*(#t218) = #t208
	#t218 = 8 + #t218
	*(#t218) = #t209
	#t218 = 8 + #t218
	*(#t218) = #t210
	#t218 = 8 + #t218
	*(#t218) = #t211
	#t218 = 8 + #t218
	*(#t218) = #t212
	#t218 = 8 + #t218
	*(#t218) = #t213
	#t218 = 8 + #t218
	*(#t218) = #t214
	#t218 = 8 + #t218
	*(#t218) = #t215
	#t218 = 8 + #t218
	*(#t218) = #t216
	#t219 = 0
	#t220 = 5
	#t221 = 0
	#t222 = 0
	#t223 = 9
	#t224 = 0
	#t225 = 6
	#t226 = 0
	#t227 = 0
	#t228 = 80
	save registers  
	stackpointer -8 
	param #t228 
	call allocmem 1
	#t228 = return_value
	stackpointer +8 
	restore registers  
	#t229 = #t228
	*(#t229) = 9
	#t229 = 8 + #t229
	*(#t229) = #t219
	#t229 = 8 + #t229
	*(#t229) = #t220
	#t229 = 8 + #t229
	*(#t229) = #t221
	#t229 = 8 + #t229
	*(#t229) = #t222
	#t229 = 8 + #t229
	*(#t229) = #t223
	#t229 = 8 + #t229
	*(#t229) = #t224
	#t229 = 8 + #t229
	*(#t229) = #t225
	#t229 = 8 + #t229
	*(#t229) = #t226
	#t229 = 8 + #t229
	*(#t229) = #t227
	#t230 = 1
	#t231 = 3
	#t232 = 0
	#t233 = 0
	#t234 = 0
	#t235 = 0
	#t236 = 2
	#t237 = 5
	#t238 = 0
	#t239 = 80
	save registers  
	stackpointer -8 
	param #t239 
	call allocmem 1
	#t239 = return_value
	stackpointer +8 
	restore registers  
	#t240 = #t239
	*(#t240) = 9
	#t240 = 8 + #t240
	*(#t240) = #t230
	#t240 = 8 + #t240
	*(#t240) = #t231
	#t240 = 8 + #t240
	*(#t240) = #t232
	#t240 = 8 + #t240
	*(#t240) = #t233
	#t240 = 8 + #t240
	*(#t240) = #t234
	#t240 = 8 + #t240
	*(#t240) = #t235
	#t240 = 8 + #t240
	*(#t240) = #t236
	#t240 = 8 + #t240
	*(#t240) = #t237
	#t240 = 8 + #t240
	*(#t240) = #t238
	#t241 = 0
	#t242 = 0
	#t243 = 0
	#t244 = 0
	#t245 = 0
	#t246 = 0
	#t247 = 0
	#t248 = 7
	#t249 = 4
	#t250 = 80
	save registers  
	stackpointer -8 
	param #t250 
	call allocmem 1
	#t250 = return_value
	stackpointer +8 
	restore registers  
	#t251 = #t250
	*(#t251) = 9
	#t251 = 8 + #t251
	*(#t251) = #t241
	#t251 = 8 + #t251
	*(#t251) = #t242
	#t251 = 8 + #t251
	*(#t251) = #t243
	#t251 = 8 + #t251
	*(#t251) = #t244
	#t251 = 8 + #t251
	*(#t251) = #t245
	#t251 = 8 + #t251
	*(#t251) = #t246
	#t251 = 8 + #t251
	*(#t251) = #t247
	#t251 = 8 + #t251
	*(#t251) = #t248
	#t251 = 8 + #t251
	*(#t251) = #t249
	#t252 = 0
	#t253 = 0
	#t254 = 5
	#t255 = 2
	#t256 = 0
	#t257 = 6
	#t258 = 3
	#t259 = 0
	#t260 = 0
	#t261 = 80
	save registers  
	stackpointer -8 
	param #t261 
	call allocmem 1
	#t261 = return_value
	stackpointer +8 
	restore registers  
	#t262 = #t261
	*(#t262) = 9
	#t262 = 8 + #t262
	*(#t262) = #t252
	#t262 = 8 + #t262
	*(#t262) = #t253
	#t262 = 8 + #t262
	*(#t262) = #t254
	#t262 = 8 + #t262
	*(#t262) = #t255
	#t262 = 8 + #t262
	*(#t262) = #t256
	#t262 = 8 + #t262
	*(#t262) = #t257
	#t262 = 8 + #t262
	*(#t262) = #t258
	#t262 = 8 + #t262
	*(#t262) = #t259
	#t262 = 8 + #t262
	*(#t262) = #t260
	#t263 = 80
	save registers  
	stackpointer -8 
	param #t263 
	call allocmem 1
	#t263 = return_value
	stackpointer +8 
	restore registers  
	#t264 = #t263
	*(#t264) = 9
	#t264 = 8 + #t264
	*(#t264) = #t173
	#t264 = 8 + #t264
	*(#t264) = #t184
	#t264 = 8 + #t264
	*(#t264) = #t195
	#t264 = 8 + #t264
	*(#t264) = #t206
	#t264 = 8 + #t264
	*(#t264) = #t217
	#t264 = 8 + #t264
	*(#t264) = #t228
	#t264 = 8 + #t264
	*(#t264) = #t239
	#t264 = 8 + #t264
	*(#t264) = #t250
	#t264 = 8 + #t264
	*(#t264) = #t261
	sudoku = #t263
	#t265 = 8
	save registers  
	stackpointer -8 
	param #t265 
	call allocmem 1
	#t265 = return_value
	stackpointer +8 
	restore registers  
	save registers  
	stackpointer -8 
	param #t265 
	call Solution.__init__ 1
	stackpointer +8 
	restore registers  
	sol = #t265
	#t266 = sol
	#t267 = sudoku
	save registers  
	stackpointer -16 
	param #t267 
	param #t266 
	call Solution.SolveSudoku 2
	#t268 = return_value
	stackpointer +16 
	restore registers  
	ifFalse #t268 jump L34
	#t269 = .str2
	save registers  
	stackpointer -8 
	param #t269 
	call print_str 1
	stackpointer +8 
	restore registers  
	#t270 = sol
	#t271 = sudoku
	save registers  
	stackpointer -16 
	param #t271 
	param #t270 
	call Solution.printGrid 2
	stackpointer +16 
	restore registers  
	jump L35

L34:
	#t272 = .str3
	save registers  
	stackpointer -8 
	param #t272 
	call print_str 1
	stackpointer +8 
	restore registers  

L35:
	leave
	return  
	endfunc 

